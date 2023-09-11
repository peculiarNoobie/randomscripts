import yaml, os, getopt, datetime, requests, json
from dotenv import load_dotenv




def modification_date(filename):
	if os.path.isfile(filename):
		last_modified_date = datetime.datetime.fromtimestamp(os.path.getmtime(filename))
	else:
		last_modified_date = datetime.datetime.fromtimestamp(0)
	return last_modified_date

load_dotenv()
path= os.getenv('confdump_path')
#directory = "PHInfrascripts\\EJBCA\\"
filter = ["OperatorCA_operators.yaml"]
errors = []
issues = []

fname = path+'validators\\Zlint_esc_spc_-_esc_spc_Validation_esc_spc_of_esc_spc_the_esc_spc_CT_esc_spc_certificate.yaml'
d = modification_date(fname)
print ("zlint file from: ")
print (d)

privatecas = [
"aafcuica2020CA",
"aafcuroot2020r1CA",
"acuityintermediateCA",
"acuityrootR1CA",
"advantagecareicaCA",
"advantagecarerootcar1CA",
"aistintca2019CA",
"aistrootcaCA",
"belfastairportica2019CA",
"belfastairportrootCA",
"cityofdurhamrootCA",
"crbgroupmicaCA",
"crbgrouprootCA",
"ctbcbankcorpusaintermediateCA",
"ctbcbankcorpusarootr1CA",
"delicatovineyardsmica2019CA",
"delicatovineyardsroot2019CA",
"dexkoglobalica2019CA",
"dexkoglobalrootCA",
"docusignica2020CA",
"docusignrootCA",
"ecadminca1sha2g2CA",
"Edenred-RootCA02",
"edirootCA",
"edirootsha2CA",
"emblemhealthintermediateCA",
"emblemhealthrootr1CA",
"eneosprivaterootca2021",
"epomachineica2019CA",
"eporootca2019CA",
"epouserica2019CA",
"esafbankprivaterootca2021CA",
"europeangnssagencyprivaterootca2021CA",
"extricprivaterootca2021",
"fifcoatlasica2020CA",
"fifcoprivaterootca2020CA",
"fourseasonshotelrootr1CA",
"grundfosrootca01g12021CA",
"gsaegicaCA",
"gsaegrootCA",
"gsaegsmimeicaCA",
"gsdemosha2g3CA",
"gshvecciotroot2018CA",
"gshvrsaiotroot2018CA",
"gvcgroupica2019CA",
"haulmerprivaterootca2021CA",
"hdsrootca2020CA",
"hertzintermediateCA",
"hertzrootR1CA",
"hitachiprivateCA",
"huntingtonbeachmicaCA",
"huntingtonbeachrootCA",
"hyperionrootCA",
"hyperionrsaCA",
"intranetssleccsha2g3CA",
"intranetsslg3CA",
"intranetsslsha2g3CA",
"isonewenglandrootr1CA",
"jlrprivicaCA",
"jlrprivrootCA",
"lxirootCA",
"ManagementCA",
"mathematicaicaCA",
"mathematicarootcar1CA",
"mindtreelimitedrootca2021CA",
"ncdorintermediateCA",
"ncdorrootR1CA",
"nyisocollaborationCA",
"nyisoexternalCA",
"nyisointernal1CA",
"nyisointernal2CA",
"organizationvalsha1g2CAT",
"prodrivetechnologiesmicaCA",
"pyronixca2020CA",
"retired_gsr7admincasha256g3CA",
"retired_gsr8admincasha256g3CA",
"roseburgintermediateCA",
"roseburgrootR1CA",
"rtiintermediateCA",
"rtirootR1CA",
"rweclientauthica",
"rweprivaterootcar1",
"rweserverauthica",
"shiseidoicaCA",
"shiseidorootCA",
"skuidclientauthCA",
"spidercloudgccmachineauthica2020CA",
"spidercloudgccprivaterootca2020CA",
"spiritaerosysicaCA",
"spiritaerosysrootcar1CA",
"stateofnhintermediateCA",
"stateofnhrootcar1CA",
"tafeswintermediateCA",
"tafeswrootR1CA",
"tkeprivaterootca2021CA",
"trustloginclientauthcaCA",
"uhsintermediateCA",
"uhsrootR1CA",
"vistaequityrootr1CA",
"wellaclientauthca2021CA",
"wellaprivaterootca2021CA",
"wellasslca2021CA",
"whitecaprootca2021CA",
"ykkapica2020CA",
"ykkaproot2020CA"
]

# Get all CAs, store as CA["dn"] = DN

# Concepts
# 
# Zlint
# A CA is properly linted by zlint if
# 1) the CA includes the validators "certification-authority.validators includes zlint"
# 2) each profile of the CA is included in the validator: "validators\zlint includes the profile"
# 
# Certlint
# Certlint must be enabled on the CA in CRL Publishers
# For each profile of the CA, certlint must be in Publishers

cas = {}
tosend=os.getenv('tosendPath')
list_of_all_cas = open(tosend+'\list_of_all_cas.txt', 'w')
for root, dirs, files in os.walk(path+'certification-authorities\\'):
	for file in files:
		# if file.endswith(".yaml") and "tafeswintermediate" in file:
		if file.endswith(".yaml"):
			ca_data = yaml.load(open(os.path.join(root, file), encoding="utf-8"), Loader=yaml.FullLoader)
			ca = ca_data['Name']
			list_of_all_cas.write(ca+"\n")
			if ca not in privatecas and "revoked" not in ca and "offline" not in ca:
				ca_dn = ca_data["Subject DN"]
				crl_publishers = []
				if "CRL Publishers" in ca_data:
					crl_publishers = ca_data["CRL Publishers"]
				validators = []
				if "Validators" in ca_data:
					validators = ca_data["Validators"]
				if ca not in cas:
					cas[ca] = {"sdn": ca_dn, "profiles": {}, "validators": validators, "crl_publishers": crl_publishers}
list_of_all_cas.close()

# Get all profiles

profiles = {}

for root, dirs, files in os.walk(path+'certificate-profiles\\'):
		for file in files:
			# if file.endswith(".yaml") and file not in filter and "ocsp" in file:
			if file.endswith(".yaml") and file not in filter:
				# print(file)
				profile_data = yaml.load(open(os.path.join(root, file), encoding='utf-8'), Loader=yaml.FullLoader)
				if profile_data["Name"] not in profiles:
					profiles[profile_data["Name"]] = profile_data["Available CAs"]
				publishers = []
				if "Publishers" in profile_data and "CertLint_Publisher" in profile_data["Publishers"]:
					publishers.append("CertLint_Publisher")

				for ca in profile_data["Available CAs"]:
					if ca not in cas:
						errors.append("CA: " + ca + " can't be found in the ca list")
					else:
						if ca not in privatecas and "revoked" not in ca and "offline" not in ca:
							cas[ca]["profiles"][profile_data["Name"]] = {"validators": [], "publishers": publishers}

# Indicate which profile is filtered by which validation

validators = ["Zlint_esc_spc_-_esc_spc_Validation_esc_spc_of_esc_spc_the_esc_spc_pre-certificate.yaml","Zlint_esc_spc_-_esc_spc_Validation_esc_spc_of_esc_spc_the_esc_spc_final_esc_spc_certificate.yaml","Zlint_esc_spc_-_esc_spc_Validation_esc_spc_of_esc_spc_the_esc_spc_CT_esc_spc_certificate.yaml"]

mapping = {
	"Zlint_-_Validation_of_the_pre-certificate.yaml": "zlint pre-cert",
	"Zlint_-_Validation_of_the_final_certificate.yaml":"zlint final-cert",
	"Zlint_-_Validation_of_the_CT_certificate.yaml":"zlint CT-cert",
	"Zlint - Validation of the pre-certificate": "zlint pre-cert",
	"Zlint - Validation of the final certificate":"zlint final-cert",
	"Zlint - Validation of the CT certificate":"zlint CT-cert",
    "Zlint_esc_spc_-_esc_spc_Validation_esc_spc_of_esc_spc_the_esc_spc_pre-certificate.yaml": "zlint pre-cert",
	"Zlint_esc_spc_-_esc_spc_Validation_esc_spc_of_esc_spc_the_esc_spc_final_esc_spc_certificate.yaml":"zlint final-cert",
	"Zlint_esc_spc_-_esc_spc_Validation_esc_spc_of_esc_spc_the_esc_spc_CT_esc_spc_certificate.yaml":"zlint CT-cert",
	"Zlint_esc_spc_-_esc_spc_Validation_esc_spc_of_esc_spc_the_esc_spc_pre-certificate.yaml": "zlint pre-cert",
	"Zlint_esc_spc_-_esc_spc_Validation_esc_spc_of_esc_spc_the_esc_spc_final_esc_spc_certificate.yaml":"zlint final-cert",
	"Zlint_esc_spc_-_esc_spc_Validation_esc_spc_of_esc_spc_the_esc_spc_CT_esc_spc_certificate.yaml":"zlint CT-cert"
}

for file in validators:
	with open (path+"validators\\"+file) as f:
		data = yaml.load(f, Loader=yaml.FullLoader)
		print(mapping[file] + " configured for "+data["If Validation Fails"])
		print(mapping[file] + " configured to "+data["If Validator Not Applicable"]+" when not applicable")
		print(mapping[file] + " configured to run at "+data["Issuance Phase"])
		print(mapping[file] + " configured from "+data["External Command"])

		for profile in data["Apply for Certificate Profiles"]:
			if profile not in profiles:
				errors.append("Profile:" + profile + " not found in profile list")
			else:
				# Get all CAs
				for ca in profiles[profile]:
					if ca not in privatecas and "revoked" not in ca and "offline" not in ca:
						# Find the profile in the ca list and mark the validator
						cas[ca]["profiles"][profile]["validators"].append(data["Name"])

# Print all profiles and their proper zlint validators enabled
zlinted_profiles = open(tosend+'\zlinted_profiles.txt', 'w')
for ca in cas:
# Check if there's really profiles
# If there's no validators enabled on the CA level, raise an issue
# If there's validators enabled, check if at least 1 profile fills this in
	validators_on_ca = {}
	if(len(cas[ca]["validators"]) > 0):
		for validator in cas[ca]["validators"]:
			validators_on_ca[validator] = 0
	if(len(cas[ca]["profiles"]) > 0):
		for profile in cas[ca]["profiles"]:
			# Check if each validator of the profile also is indicated as validator on the CA above
			validators_on_profile_and_ca = []
			for validator in cas[ca]["profiles"][profile]["validators"]:
				if validator in cas[ca]["validators"]:
					validators_on_profile_and_ca.append(mapping[validator])
					# Mark this validator as configured on the profile
					validators_on_ca[validator] = validators_on_ca[validator] + 1
				else:
					issues.append("Validator: {0} enabled on profile: {1} but not on CA: {2}".format(mapping[validator],profile,ca))
					# issues.append("Validator: " + validator + " enabled on profile: " + profile + " but not on CA: " + ca)
			# Check if each validator of the ca is also enabled on this profile
			for validator in cas[ca]["validators"]:
				if validator not in cas[ca]["profiles"][profile]["validators"]:
					# except for CT for OCSP profiles
					if "ocsp" in profile and "CT" in validator:
						True
					else:
						issues.append("Validator: {0} configured on CA: {1} but not on profile: {2}".format(mapping[validator],ca,profile))
			if(len(validators_on_profile_and_ca)>0):
				zlinted_profiles.write(ca + ";" + profile + ";" + str(len(validators_on_profile_and_ca)) + ";" + ",".join(validators_on_profile_and_ca)+"\n")
	# Find all validators that were configured on the CA but not used in a profile
	for validator in validators_on_ca:
		if validators_on_ca[validator] == 0:
			issues.append("Validator: {0} configured on CA: {1} but not used in a profile of that CA".format(mapping[validator],ca))
zlinted_profiles.close()

# Print all profiles and their proper certlint publishers enabled
certlinted_profiles = open(tosend+'\certlinted_profiles.txt', 'w')
for ca in cas:
	# Check if there's really profiles
	if(len(cas[ca]["profiles"]) > 0):
		for profile in cas[ca]["profiles"]:
			# Check if the CA includes CertLint_Publisher in the crl_publisher and the profile includes CertLint:
			if "CertLint_Publisher" in cas[ca]["crl_publishers"]:
				if "CertLint_Publisher" in cas[ca]["profiles"][profile]["publishers"]:
					certlinted_profiles.write(ca + ";" + profile + ";" + str(len(cas[ca]["profiles"][profile]["publishers"])) + ";" + ",".join(cas[ca]["profiles"][profile]["publishers"])+"\n")
				else:
					issues.append("Certlint enabled on CA: {0} but not on profile: {1}".format(ca,profile))
			# Check if the profile includes Certlint but the CA doesn't
			if "CertLint_Publisher" in cas[ca]["profiles"][profile]["publishers"] and "CertLint_Publisher" not in cas[ca]["crl_publishers"]:
				issues.append("Certlint enabled on profile: {0} but not on CA: {1}".format(profile,ca))
certlinted_profiles.close()
# print(json.dumps(cas,indent = 6))

for issue in issues:
	print("Issue: " + issue)

# Print signing algorithms

from pathlib import Path
import glob

sgsigalg = open(tosend+"\stasigalg.txt","w+")
sgsigalg2 = open(tosend+"\signing-algs.csv","w+")
certprofilepath = path+'certificate-profiles\*.yaml' 
cadetails = path+'certification-authorities' 
cryptotoken = path+'crypto-tokens\ORCA_OCS_Card.yaml'
files=glob.glob(certprofilepath) 
cas=0
#sgsigalg.write("Opened") 
sgsigalg2.write("Certificate Profile,Alg Used,CA Used,CA Key Alg,CA Key\n") 
for file in files: 
	#sigalg.write(file + "\n")
	with open(file, "r", encoding='utf-8') as a_file:
		
		for line in a_file:
		#sigalg.write ("here")
			if line.find("Name:") == 0:
				
				stripped_line = line.strip()
				#print()
				#print('Profile: ', stripped_line.replace('Name: ', ''))
				sgsigalg2.write(stripped_line.replace('Name: ', '') + ", ")
			if cas==1:
				stripped_line = line.strip()
				cas=0
				sgsigalg.write(stripped_line + " - ")
				cafilename=stripped_line.replace(" ","_")
				#print(cafilename)
				if cafilename == "-_-2042690451":
					sgsigalg2.write("\n")
					break
				CAfile = cadetails + "\\" + cafilename[2:] + ".yaml"
				CAfil = Path(CAfile)
				if CAfil.is_file():
					with open(CAfile, "r", encoding='utf-8') as c_file:
						fnd=0

						for line2 in c_file:
							#linting = ","
							#if line2.find("zlint") >= 0:
							#	linting = ", zlint enabled"
							if line2.find(" Certificate Signing Key:") >= 0:
								fnd=1
								#print (line2[2:],end="")
								linene=line2[2:]
								linene=linene.strip()
								sgsigalg2.write(linene + ", ")
								with open(cryptotoken, "r", encoding='utf-8') as ct_file:
									found = 0
									for line3 in ct_file:
										alias = "Alias: " + line2[27:80]
										if line3.find(alias) >= 0:
											#print (line3[2:])
											found = 1
											nextline = ct_file.readline()[2:]
											if nextline.find("Key Algorithm:") == -1:
												nextline = ct_file.readline()[2:]
											nextline = nextline.strip()
											sgsigalg2.write(nextline + ", ")
											sgsigalg2.write(ct_file.readline()[2:])
											break
									if found == 0:
										sgsigalg2.write("\n")
							
							
			if line.find("Available CAs:") == 0:
				cas=1
			if line.find("Signature Algorithm:") >= 0:
				stripped_line = line.strip()
				sgsigalg.write(stripped_line + "\n")
				#print(stripped_line)
				sgsigalg2.write(stripped_line + ", ")
sgsigalg.close()				
os.remove(tosend+"\stasigalg.txt")


ctlogfolder = path+'ct-logs\\*.yaml'  
files=glob.glob(ctlogfolder)
stringtostrip = path+'ct-logs\\' 
stringcloudflare = 'ct.cloudflare.com-logs-'
stringgoogle = 'ct.googleapis.com-logs-'
stringcomodo = '.ct.comodo.com'
stringdigicert = '.ct.digicert.com-log'
stringending = '-ct-v1'
from datetime import date
ctthisyear = 'Log Sharding Year: ' + str(date.today().year)
nextyear = (date.today().year) + 1
ctnextyear = 'Log Sharding Year: ' + str(nextyear)
nextnextyear = (date.today().year) + 2
ctnextnextyear = 'Log Sharding Year: ' + str(nextnextyear)
all_logs = []
print("\n\n" + ctthisyear + " CT Logs\n")
for file in files:
    with open(file) as f:
        contents = f.read()
        ct_name = file.replace(stringtostrip,'').replace('.yaml','').replace(stringcloudflare,'').replace(stringgoogle,'').replace(stringcomodo,'').replace(stringdigicert,'').replace(stringending,'')
        if 'Label: Unlabeled' in contents:
            if ctthisyear in contents:
                print(ct_name)
                all_logs.append(ct_name)
            if 'Log Sharding Year: null' in contents:
                print(ct_name)
                all_logs.append(ct_name)
        if 'Label: Mandatory' in contents:
            if ctthisyear in contents:
                print(ct_name + ": Mandatory")
                all_logs.append(ct_name)
            if 'Log Sharding Year: null' in contents:
                print(ct_name + ": Mandatory")
                all_logs.append(ct_name)
print("\n\n" + ctnextyear + " CT Logs\n")
for file in files:
    with open(file) as f:
        contents = f.read()
        ct_name = file.replace(stringtostrip,'').replace('.yaml','').replace(stringcloudflare,'').replace(stringgoogle,'').replace(stringcomodo,'').replace(stringdigicert,'').replace(stringending,'')
        if 'Label: Unlabeled' in contents:
            if ctnextyear in contents:
                print(ct_name)
                all_logs.append(ct_name)
            if 'Log Sharding Year: null' in contents:
                print(ct_name)
                all_logs.append(ct_name)
        if 'Label: Mandatory' in contents:
            if ctnextyear in contents:
                print(ct_name + ": Mandatory")
                all_logs.append(ct_name)
            if 'Log Sharding Year: null' in contents:
                print(ct_name + ": Mandatory")
                all_logs.append(ct_name)
print("\n\n" + ctnextnextyear + " CT Logs (ie usable for full term certificates after 29 November " + str(date.today().year) + ")\n")
for file in files:
    with open(file) as f:
        contents = f.read()
        ct_name = file.replace(stringtostrip,'').replace('.yaml','').replace(stringcloudflare,'').replace(stringgoogle,'').replace(stringcomodo,'').replace(stringdigicert,'').replace(stringending,'')
        if 'Label: Unlabeled' in contents:
            if ctnextnextyear in contents:
                print(ct_name)
                all_logs.append(ct_name)
            if 'Log Sharding Year: null' in contents:
                print(ct_name)
                all_logs.append(ct_name)
        if 'Label: Mandatory' in contents:
            if ctnextnextyear in contents:
                print(ct_name + ": Mandatory")
                all_logs.append(ct_name)
            if 'Log Sharding Year: null' in contents:
                print(ct_name + ": Mandatory")
                all_logs.append(ct_name)
URL = "https://www.gstatic.com/ct/log_list/v2/log_list.json"
response = requests.get(URL)
open("log_list.json", "wb").write(response.content)
print("\n\nCurrently available (usable) CT Logs\n")
all_available_logs = []
with open(r'log_list.json') as jsondata:
    operators_list = json.load(jsondata)
    o = 0
    for operators in operators_list['operators']:
        for logs in operators_list['operators'][o]['logs']:
            if "usable" in logs['state']:
                print(logs['description'])
                all_available_logs.append(logs['description'])
            if "qualified" in logs['state']:
                print(logs['description'] + " - Qualified")
                #all_available_logs.append(logs['description'])
        o = o + 1                
			
print("\n\nCurrently unused but available (usable) CT Logs - Google do not accept Qualified\n")
all_logs = list(set(all_logs))
all_available_logs = list(set(all_available_logs))
for i in all_available_logs:
    used = "no"
    for j in all_logs:
            logtofind = "'" + j + "'"
            logdtofind = " " + j + " "
            if ((i.lower().find(logtofind) != -1) or (i.lower().find(logdtofind) != -1)):
                #print("strange " + i.lower() + " - " + logtofind + " " + logdtofind)
                used = "yes"
    if used == "no":
        #print("strange " + i.lower() + " - " + logtofind + " " + logdtofind)
        print (i)  
URL = "https://valid.apple.com/ct/log_list/current_log_list.json"
response = requests.get(URL)
open("current_log_list.json", "wb").write(response.content)
print("\n\nApple Currently available (usable) CT Logs\n")
all_available_logs = []
with open(r'current_log_list.json') as jsondata:
    operators_list = json.load(jsondata)
    o = 0
    for operators in operators_list['operators']:
        for logs in operators_list['operators'][o]['logs']:
            if "usable" in logs['state']:
                print(logs['description'])
                strippedspace = logs['description'].replace(" 20", "20")
                all_available_logs.append(strippedspace)
            if "qualified" in logs['state']:
                print(logs['description'] + " - Qualified")
                all_available_logs.append(logs['description'])
        o = o + 1                
			
print("\n\nApple Currently unused but available (usable) CT Logs - Apple 'may' accept Qualified\n")
all_logs = list(set(all_logs))
all_available_logs = list(set(all_available_logs))
#print(all_available_logs)
for i in all_available_logs:
    used = "no"
    for j in all_logs:
            logtofind = "'" + j + "'"
            logdtofind = " " + j + " "
            if ((i.lower().find(logtofind) != -1) or (i.lower().find(logdtofind) != -1)):
                #print("strange" + i.lower() + " - " + logtofind + " " + logdtofind)
                used = "yes"
    if used == "no":
        if i == "Google 'Xenon2023 log":
            print (i + " : False positive - Apple are ridiculous and need to learn to close quotes") 
        else:
            print (i)
print ("\n\nAudit check ended")