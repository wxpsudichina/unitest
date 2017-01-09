#coding=GBK  
import requests
import unittest
import json
import os
import numbers
class testApp(unittest.TestCase):
    def setUp(self):
        self.base_url = 'http://10.110.1.55:8081/1.0/'
        self.cat_list_uri = 'cat/list'
        self.cat_app_uri = 'cat/app/'
        self.file_prop_uri = 'file/'
        self.dlwd_icon_uri = 'app/icon/cont/'
        self.dlwd_screen_uri = 'app/screen/cont/'
        self.dlwd_apk_uri = 'app/cont/'
        self.comment_add_uri = 'app/c/' #  POST /app/c/{app_id}
        self.comment_get_uri = 'app/screen/cont/' #GET app/c/list/{app_id}?pos={pos}&limit={limit}
        self.cat_listId = []   #data
        self.cat_len = 0;
        self.cat_listName=[]   #name
        self.cat_listSeq_num=[]   #seq_num
        self.cat_listFile_size=[]   #file_size
        self.cat_listMime_type=[]   #mime_type
        self.cat_listParent_id=[]    #parent_id
        self.cat_listMime_type=[]   
        self.list_app_id=[]
        self.list_icon_id=[]
        self.list_apk_id=[]
        self.list_screen_id=[]

    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri        
        response = requests.get(url)                
        jResp = response.json()  
        
        jData = jResp["data"]

        for jCat in jData:

            self.cat_listId.append(jCat['id'])                                
            self.cat_listName.append(jCat['name'])                       
            self.cat_listSeq_num.append(jCat['seq_num'])   
                             
            self.cat_listFile_size.append(jCat['file_size']) 
                            
            self.cat_listMime_type.append(jCat['mime_type'])                        
            self.cat_listParent_id.append(jCat['parent_id'])            
            self.cat_listMime_type.append(jCat['mime_type'])        
                   



        self.cat_listParent_idRemSm=list(set(self.cat_listParent_id))
        self.cat_listId.append(u'0')

       
        for parent_Id in self.cat_listParent_idRemSm:
            self.cat_listId.remove(parent_Id)
#        print self.cat_listId
        
        print 'ȥ��parent_id��id�б�'
        print self.cat_listId
  
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '��%d��Ӧ��' %i
            print '��ҽ�õ�id��%r '  %category_id 
           
            i=i+1
            self.get_app_info(category_id)  
              

    def get_app_info(self, category_id):
        self.list_tmp_id=[] 
        url = self.base_url + self.cat_app_uri+category_id
        print url
        #print self.cat_list
        response = requests.get(url)
        self.assertEqual(response.status_code, 200)
        print 'app��״̬����200'

        jResp = response.json()
        
        result_code = jResp["result_code"]
        self.assertEqual(result_code, 200) 
        print 'result_codeֵΪ200'
        
        appNum_limit = jResp["limit"]
        appNum_total=jResp['total'] 
        self.assertLessEqual(appNum_limit, appNum_total) 
        print 'limitС�ڵ���total'

 
        jData = jResp["data"]

        for appData in jData:
            
                print 'app_id'
                print appData['id']
                self.list_app_id.append(appData['id'])
                self.list_tmp_id.append(appData['id'])
                
                
                print 'app_name'
                print appData['app_name']
                print 'package_name'
                print appData['package_name']
                print 'version_name'
                print appData['version_name']
                print 'version_code'
                print appData['version_code']
                print 'cat'
                print appData['cat']
                print 'price'
                print appData['price']
                print 'app_permit'
                print appData['app_permit']
                
                print 'apk_id'
                print appData['apk_id']
                self.list_apk_id.append(appData['apk_id'])
                
                print 'icon_id'
                print appData['icon_id']
                self.list_icon_id.append(appData['icon_id'])
            
                print 'signature'
                print appData['signature']
            

            
                print 'screen_id'
                print appData['screen_id']
                self.list_screen_id.append(appData['screen_id'])
                
               



        print 'app_id���' 
        for   app_id in self.list_app_id:
                                  
            print app_id
            print '\t' 
            
        print 'apk_id���'    
        for apk_id in self.list_apk_id:
             
            print apk_id
            print '\t' 

           
        print 'icon_id���'     
        for icon_id in self.list_icon_id:
            
            print icon_id
            print '\t' 

           
        print 'screen_id���'    
        for screen_id in self.list_screen_id:
             
            print screen_id
            print '\t' 
            
        self.assertLessEqual(appNum_limit, len(self.list_tmp_id))
        print '��Ŀ��������limit'   