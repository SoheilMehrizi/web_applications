from nylas import APIClient
import requests
from web.models import API_KEYs

#nylas Platform Connection
def nylas_EtoE_Messenger(context):
    Auth = API_KEYs.objects.get(platform_name = "nylas")
    CLIENT_ID     = Auth.CLIENT_ID
    CLIENT_SECRET = Auth.CLIENT_SECRET
    ACCESS_TOKEN  = Auth.ACCESS_TOKEN
    nylas = APIClient(
        CLIENT_ID,
        CLIENT_SECRET,
        ACCESS_TOKEN,
    )
    message       = f"""name : {context["name"]}  |  
            Company_name : {context["co_name"]}  |  
            Tendency : {context["tendency"]}  |  
            email_address : {context["email"]}  |  
            Phone : {context["phone"]}  |  
            Service : {context["service"]}  |  """

    draft = nylas.drafts.create()
    draft.subject = "Project_Registration"
    draft.body    = message
    draft.to      = [{'name': 'Soheil', 'email': 'mehrizisoheil@gmail.com'}]
    draft.send()
    print(draft)
    return(draft)


#Pakat Platform Connection
def Pakat_email_sender(context):
    """Email Sender Agent"""

    URL = "https://api.pakat.net/v3/smtp/email"

    try:
        API_info = API_KEYs.objects.get(Location = URL)
        API_KEY = API_info.API_KEY
    except Exception:
        print(f"Error: {Exception}")
    message = f"""name:{context["name"]} \n
                 Company_name:{context["co_name"]} \n
                 Tendensy :{context["tendency"]} \n
                 email_address: {context["email"]}\n
                 Phone:{context["phone"]}\n
                 Service:{context["service"]}\n"""
    print (API_KEY)
    data = {
        "sender"  :{"name" :"Test",
                   "email":"trial@ttrial.pick-inside-956.com"},

        "to"      :[{'name':'SoheilMEHRIZI',
                    'email':"mehrizisoheil@gmail.com",
                   },
                  ],
        "htmlContent" : "Mandatory",

        "subject" : "A New Project",

        "textContent" : message
        }
    headers = {'api-key': API_KEY}
    try:
        r = requests.post(URL,params=data, headers=headers)
        print(r)
        return True
    except Exception:
        print(f"Error : {Exception}")
        return False

