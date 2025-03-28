# Meraki Reboot AP
 Meraki Python API script to reboot all the Meraki APs of an organisation without using Meraki switches :

<p align="center">
<img width="800" alt="image" src="https://github.com/user-attachments/assets/1a3707a2-5064-41a9-a433-6ab6bb526cf4" />
</p>

## Prerequisites
- Meraki Dashboard access
- Meraki API key
- Meraki organisation ID
- Meraki AP

## Get started
1. Clone or download this repo
```console
git clone https://github.com/xaviervalette/meraki-reboot-ap

```
2. Install required packages
```console
python3 -m pip install -r requirements.txt
```
3. Add a ```config.yml``` file as follow:
```diff
└── meraki_reboot_ap/
+   ├── config.yml
    ├── requirements.txt
    └── src/
         └── main.py  
```
4. In the ```config.yml``` file, add the following variables:
```yaml
#config.yml
---
apiKey: "<yourApiKey>"
organisationId: "<yourOrgId>"
...

```

5. Now you can run the code by using the following command:
```console
python3 src/main.py
```

## Output
The output should be as followed:
```console
(.venv) xvalette@XVALETTE-M-06WY meraki-reboot-ap % python3 src/main.py
AP AAAA-AAAA-AAAA reboot status 202
AP BBBB-BBBB-BBBB reboot status 202
[...]
```

The status code 202 is expected, it means that the request has been accepted for processing, but the processing has not been completed.

If you get a status code 429, it means that you are rate limited, because you already run the code during the same minute

```console
(.venv) xvalette@XVALETTE-M-06WY meraki-reboot-ap % python3 src/main.py
AP AAAA-AAAA-AAAA reboot status 429
AP BBBB-BBBB-BBBB reboot status 429
```

You can check on the Meraki dashboard that the given AP are reloaded :

<img width="274" alt="image" src="https://github.com/user-attachments/assets/e08ac407-be8a-4104-8316-ed918c44986e" />
<img width="1180" alt="image" src="https://github.com/user-attachments/assets/b7f80aeb-546e-4507-92fc-1078e36523f6" />



