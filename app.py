import requests
import json
import pyfiglet
from time import sleep

# SYSTEM COLOR CODES
W = '\x1b[38;5;231m'  # Dark white 
G = '\x1b[1;32m'      # Green
B = '\x1b[38;5;18m'   # Dark Blue
b = '\x1b[38;5;153m'  # Light blue 
Y = '\x1b[38;5;226m'  # Dark yellow

logo = pyfiglet.figlet_format("  INTELLI-SYNTH")
print(G + logo + W)
print(f"    {Y}RESEARCH FRAMEWORK ➩ {G}AI-MEDIA SYNTHESIS CORE")
print(f"    {Y}PRINCIPAL ANALYST  ➩ {G}ARYAN KACHER\n")
print(f"{B}------------------------------------------------------------{W}\n")

# Interactive Loop to Prevent AWS Gateway Throttling
while True:
    Description = input(f"{W}ENTER PROMPT (or type 'exit' to quit) {Y}➩ {b}")
    if Description.lower() == 'exit':
        print("[*] Terminating synthesis channels...")
        break
        
    print(f"{Y}[*] Dispatching payload to serverless matrix wrapper...{W}")
    
    headers = {
        'accept': '*/*',
        'accept-language': 'en-US,en;q=0.9,ar;q=0.8',
        'origin': 'https://www.writecream.com',
        'priority': 'u=1, i',
        'referer': 'https://www.writecream.com/',
        'user-agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36',
    }
    
    params = {
        'prompt': Description,
        'aspect_ratio': '16:9',
        'link': 'writecream.com',
        'description': Description,
    }
    
    try:
        response = requests.get(
            'https://1yjs1yldj7.execute-api.us-east-1.amazonaws.com/default/ai_image',
            params=params,
            headers=headers,
            timeout=15
        )

        response_data = response.json()
        image = response_data.get('image_link', 'No image link Found ')
        attempt = response_data.get('second', 'No attempt Found ')
        status = response_data.get('status', 'No status Found ')
        base64_data = response_data.get('base64', 'No base64 Found ')
        
        print(f'''
{B}[+] ======================================================== [+]
{G}    TELEMETRY RESPONSE DISPATCHED SUCCESSFUL - VALID DATA STRUCT
{B}[+] ======================================================== [+]
    {Y}➩ IMAGE RESOURCE NODE : {W}{image}
    {Y}➩ BASE64 STRING SEG  : {W}{base64_data[:40]}... [TRUNCATED]
    {Y}➩ TRANSACTION STATUS : {W}{status}
    {Y}➩ COMPUTE ATTEMPTS   : {W}{attempt}
{B}[+] ======================================================== [+]
        ''')
    except Exception as e:
        print(f"\n[ - ] Network timeout or gateway restriction triggered: {str(e)}\n")
        
    print(f"\n{B}[*] System cooling down for network safety...{W}\n")
    sleep(2)
  
