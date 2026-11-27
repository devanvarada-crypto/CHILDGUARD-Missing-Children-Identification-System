from django.urls import path
from.import views
urlpatterns=[
    path('',views.web,name="newweb"),#home page
    path('index/',views.index,name="index"),#index page
    path('register/',views.userregister,name="register"),#userregister
    path('login/',views.login,name="login"),#userlogin
    path('userhome/',views.home,name="userhome"),#userhome
    path('userprofile/',views.profile,name="userprofile"),#user profile
    path('helplineregister/', views.helpline_register_view, name='helplineregister'),#helpregistration
    path('helplinelogin/',views.loginhelpline,name="helplinelogin"),#helplogin
    path('helplinehome/',views.homehelp,name="helplinehome"),#helphome
    path('helplineprofile/',views.profilehelp,name="helplineprofile"),
    path('regsociety/',views.social_register,name="regsociety"),#societyregistration
    path('societylogin/',views.loginsociety,name="societylogin"),#societylogin 
    path('societyhome/',views.homesociety,name="societyhome"),#societyhome
    path('societyprofile/',views.profilesociety,name="societyprofile"),#societyprofile
    path('adminhome/',views.homeadmin,name="adminhome"),#societyhome
    path('adminlogin/',views.loginadmin,name="adminlogin"),#adminlogin
    path('logout/',views.logout,name="logout"),#logout


    path('userlist/',views.userlist,name="userlist"),#admin side users list
    path('deleteuser/<int:id>/',views.deleteuser,name="deleteuser"),#admin side delete users 
    path('helplist/',views.helplist,name="helplist"),#admin side helpers list
    path('deletehelp/<int:id>/',views.deletehelp,name="deletehelp"),#admin side delete helps
    path('societylist/', views.societylist, name='societylist'),
    path('deletesociety/<int:id>/', views.deletesociety, name='deletesociety'),

    
    path('child_missing_form/', views.missing_child_form, name="child_missing_form"),
    path('submit_missing_case/', views.submit_missing_case, name="submit_missing_case"),
    path('case_success/', views.case_success, name='case_success'),


    #profile edit 
   
    path('editprofilehelp/', views.editprofilehelp, name='editprofilehelp'),
    path('editprofilesociety/', views.editprofilesociety, name='editprofilesociety'),
    path('editprofileuser/', views.editprofile, name='editprofileuser'),




    
    # Admin – Case Management
    path('admin_case_list/', views.admin_case_list, name='admin_case_list'),
    path('delete_case/<int:id>/', views.admin_case_list, name='delete_case'),
    # path('verify_case/<int:id>/', views.verify_case, name='verify_case'),
    # path('unverify_case/<int:id>/', views.unverify_case, name='unverify_case'),
    


    # Helpline – Case Management

    # path('help-line_case_list/', views.helpline_cases, name='helpline_case_list'),
    
    path('helpline_home/', views.helpline_home, name='helpline_home'),
    path('user-helplines/', views.user_helpline_list, name='user_helpline_list'),
    path('child_detection_map/', views.child_detection_map, name='child_detection_map'),
    path('get_helplines/', views.get_helplines, name='get_helplines'),
    path('get_child_location/', views.get_child_location, name='get_child_location'),



   #case list of user
    path('user_missing_cases/', views.user_missing_cases,name='user_missing_cases'),
    path('edit_missing_case/<int:case_id>/', views.edit_missing_case,name='edit_missing_case'),
    path('delete_missing_case/<int:case_id>/', views.delete_missing_case,name='delete_missing_case'),
    



    path('helpline_case_list/', views.helpline_case_list, name='helpline_case_list'),
    path('approve_case/<int:case_id>/', views.approve_case,name='approve_case'),
    path('mark_found/<int:case_id>/', views.mark_found,name='mark_found'),
    path('helpline_delete_case/<int:case_id>/', views.helpline_delete_case,name='helpline_delete_case'),





#helpline->society->helpline

    path('send_alert_to_society/<int:case_id>/', views.send_alert_to_society, name='send_alert_to_society'),
    path('society_alert_list/', views.society_alert_list,name='society_alert_list'),
    path('report_child_found/<int:alert_id>/', views.report_child_found,name='report_child_found'),
    path('helpline_alert_reports/', views.helpline_alert_reports,name='helpline_alert_reports'),
    path('alerted-societies/<int:case_id>/', views.alerted_society_list,name='alerted_society_list'),

#deep face
    path('helpline/ai-verify/<int:alert_id>/', views.ai_face_verify,name='ai_face_verify'),

] 

    
