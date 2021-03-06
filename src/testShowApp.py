#coding=GBK
import requests
import unittest
import json
import os
import numbers
class testShowApp(unittest.TestCase):
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
        self.get_commentlist_uri='app/c/list/'###########新加
        self.get_app_allinfo_uri='app/'
       
        
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
        
        self.comment_id=[] 
        self.comment_app_id=[]    
        self.comment_msg=[]   
        self.comment_ip=[] 
        self.comment_stars=[] 
        self.comment_create_date=[] 
        
#第一次测试   10.110.1.55:8081/1.0/cat/list/cat/list
    def test1_cat_list_api(self):
        url = self.base_url + self.cat_list_uri        
        response = requests.get(url)                
        jResp = response.json()  
        
        jData = jResp["data"]
#把data中的id部分依次遍历，放入到self.cat_list中
        for jCat in jData: 
            self.cat_listId.append(jCat['id'])                     
            self.cat_listParent_id.append(jCat['parent_id'])            
       
        self.cat_listParent_idRemSm=list(set(self.cat_listParent_id))
        self.cat_listId.append(u'0')

#删除在id中的parent_id        
        for parent_Id in self.cat_listParent_idRemSm:
            self.cat_listId.remove(parent_Id)

#依次循环带入排除parent_id的list——id进行app测试     
        i=1    
        for category_id in self.cat_listId: 
            print '\t'           
            print '测试第%d个应用' %i
            print 'cat_id测试的ID是%r '  %category_id 
           
            i=i+1
            self.get_app_info(category_id)  
        
        
       
        for  app_id in self.list_app_id:                               
            print app_id
            self.get_comment_list(app_id)
            print '\t' 
            

                    
#主要作用是将去除parentid的id放在数组中供后期的调用
             
#第二次测试        10.110.1.55:8081/1.0/cat/app/app_id
#循环遍历，将app_id,apk_id,icon_id,scree——id全部放入数组
    def get_app_info(self, category_id):
        
        url = self.base_url + self.cat_app_uri+category_id
#        print url       
        response = requests.get(url)
        jResp = response.json()
        jData = jResp["data"]
        for appData in jData:            
                
                self.list_app_id.append(appData['id'])               


    def get_comment_list(self, app_id):
        
#        a=input("请输入pos的值")
#        b=input("请输入limit的值")
#        self.commentcontent='?pos=%d&limit=%d' %(a,b)
        
        ###########此处需要修改
        
        url = self.base_url + self.get_app_allinfo_uri + app_id#+self.commentcontent #http://10.110.1.55:8081/1.0/file/
        print '陆正飞  本次测试的URL是'
        print url
        
        response = requests.get(url) 
        self.assertEqual(response.status_code, 200) #判断返回码是否等于200
        print '服务器响应码是200'
        #print self.cat_list
        jResp = response.json()  
        result_code = jResp["result_code"]        
        self.assertEqual(result_code, 200) #判断result_code是否等于200
        print 'result_code的结果是200' 
#        print result_code       
        
        
          
             
              
        jData = jResp["data"]
        
        print "评论的id是。。。"                     
        print jData['id']
            
        print "评论的app_name。。。"            
        print jData['app_name']
            
        print "评论的package_name是。。。"            
        print jData['package_name']
            
        print "评论的version_name是。。。"
        print jData['version_name']
            
        print "评论的version_code是。。。"
        print jData['version_code']
            
        print "评论的cat是。。。"
        print jData['cat']
        
        print "评论的app_desc是。。。"
        print jData['app_desc']
        
        print "评论的version_desc是。。。"
        print jData['version_desc']
        
        print "评论的cprice是。。。"
        print jData['price']
        
        print "评论的app_permit是。。。"
        print jData['app_permit']
        
        print "评论的apk_id是。。。"
        print jData['apk_id']
        
        print "评论的icon_id是。。。"
        print jData['icon_id']
        
        print "评论的screen_id是。。。"
        print jData['screen_id']
        
        print "评论的signature是。。。"
        print jData['signature']
        
        print "评论的file_size是。。。"
        print jData['file_size']
        
        print "评论的download_count是。。。"
        print jData['download_count']
        
        print "评论的create_date是。。。"
        print jData['create_date']
        
        print "评论的mod_date是。。。"
        print jData['mod_date']
        
        print "评论的purchase是。。。"
        print jData['purchase'] 
  