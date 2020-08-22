from django.http import HttpResponseRedirect,HttpResponse
from django.shortcuts import render
from recherche.scraping import linkdin,facebook,twitter,analyze_sentiment_twitter,analyze_sentiment,clean_tweet

def recherche(request):
    if request.method == 'GET' and 'connecte' in request.session:       
        nom = request.session['nom']
        prenom = request.session['prenom'] 
        ville = request.session['ville'] 
        pays = request.session['pays'] 
        company = request.session['company']
        aboutMe = request.session['aboutMe']
        emailRec = request.session['emailRec']
        return render(request, 'recherche/rechercher.html', locals())
    else:
        return HttpResponseRedirect('/')

def profile(request):
    if request.method == 'GET' and 'connecte' in request.session:
        nom = request.session['nom']
        prenom = request.session['prenom'] 
        ville = request.session['ville'] 
        pays = request.session['pays'] 
        company = request.session['company']
        aboutMe = request.session['aboutMe']
        emailRec = request.session['emailRec']
        return render(request, 'recherche/profile.html', locals())
    else:
        return HttpResponseRedirect('/')

def creativeTeam(request):
    if request.method == 'GET' and 'connecte' in request.session:
        nom = request.session['nom']
        prenom = request.session['prenom'] 
        ville = request.session['ville'] 
        pays = request.session['pays'] 
        company = request.session['company']
        aboutMe = request.session['aboutMe']
        emailRec = request.session['emailRec']
        return render(request, 'recherche/creativeTeam.html', locals())
    else:
        return HttpResponseRedirect('/')


def candidate(request):    
    if 'connecte' in request.session:
        facebook_name = request.GET['facebook_name']
        linkdin_name = request.GET['linkdin_name']
        twitter_name = request.GET['twitter_name']
        compter_linkdin = 0
        compter_twitter = 0
        compter_facebook = 0
        #var2=facebook(search)
        ### Facebook ###
        facebook_dict = facebook(facebook_name)
        if facebook_dict["photos"] != "None":
            compter_facebook += 10
        if facebook_dict["videos"] != "None":
            compter_facebook += 10
        if facebook_dict["sports"] != "None":
            compter_facebook += 10
        if facebook_dict["music"] != "None":
            compter_facebook += 5
        if facebook_dict["books"] != "None":
            compter_facebook += 5
        if facebook_dict["likes"] != "None":
            compter_facebook += 10

        ### Linkdin ###
        linkdin_dict = linkdin(linkdin_name)
        info = linkdin_dict["info"]
        if info != "None":
            compter_linkdin += 5          
        education = linkdin_dict["education"]
        if education != "None":
            compter_linkdin += 15
        experience = linkdin_dict["education"]
        if experience != "None":
            compter_linkdin += 10
        competences = linkdin_dict["competences"]
        if competences != "None":
            compter_linkdin += 20
            dev_web = ['HTML','JavaScript', 'php','Php', 'PHP' 'HTML5','css','Css', 'Twitter Bootstrap', 'CSS', 'Javascript','Node.js', 'JEE','Java Enterprise Edition', 'Servlet', 'jsf', 'JSF', 'Hibernate', 'Struts', 'Spring', 'Spring Boot','Bootstrap', 'Bulma', 'JSFoundation', 'Uikit', 'Susy', 'Materialize', 'Pure.css', 'less', 'Angular', 'Vue.js', 'React', 'EmberJs', 'Next', 'Python', 'Java', 'Php', 'AngularJs', 'MeteorJS', 'CodeIgniter', 'Laravel', 'Ruby', 'RubyOnRails', 'CakePHP', 'Django', 'WordPress', 'Magento']
            dev_mobile = ['Java', 'Android', 'RIM', 'Symbian', 'Microsoft', 'Bada', 'Windows Phone', 'iOS', 'Kotlin', 'ReactNative', 'ObjectifC', 'Swift', 'C#', 'Xamarin', 'Sencha', 'Appcelerator', 'Ionic', 'Framework 7', 'AppWatch','PhoneGap', 'HeadSpin', 'Buddy', 'Mobincube', 'Longrange', 'Qt', 'Alpha Anywhere', 'KendoUI', 'Mobile Angular UI', 'NativeScript', 'OnsenUI', 'FireBase', 'Swiftic', 'EasyAr']
            dev_desktop = ['C#', 'Linx', 'Atom', 'Swing', 'JavaFX', 'Java', 'Buddy', '.Net', 'Xamarin', 'Apple', 'Cocoa', 'Electron']
            GL = ['Agile','Design Pattern', 'Scrum', 'Design Patterns', 'UP', 'RUP', 'UML', 'Analyse SI', 'Merise']
            DS = ['Java', 'R','Analyse de données statistiques', 'Python', 'Big data','BI','Analyse des données', 'AI', 'Artificial Intelligence', 'Business Intelligence','Intelligence artificielle', 'Data science','Data Science', 'SAS', 'Apache Spark', 'BigML', 'D3.js', 'MATLAB', 'Excel', 'ggplot2', 'Tableau', 'Jupyter', 'Matplotlib', 'NLTK', 'Scikit-learn', 'TensorFlow', 'Weka', 'Summary', 'online analytical processing', 'OLAP', 'mobile BI ', 'real-time BI', 'operational BI', 'cloud', 'open-source BI', 'collaborative BI', 'tableaux de bord', 'location intelligence', 'data visualisation', 'Power BI', 'SAP', 'MicroStrategy', 'Datapine', 'Yellowfin BI', 'QlikSense', 'Zoho Analytics', 'Sisense', 'Microsoft Power BI', 'Looker', 'Clear Analytics', 'Tableau', 'Oracle BI', 'Domo', 'IBM Cognos Analytics']
            langages = ['Java','JAVA', 'JavaScript', 'Python','php', 'PHP', 'C', 'C++', 'C#', 'Javascript', 'Visual Basic', 'Cobol', 'Assembleur', 'Lisp', 'Perl', 'Pascal', 'XSLT']
            data_bases = ['SQL', 'PLSQl', 'MySQL', 'SQLServer', 'SQLite', 'Oracle DB', 'PostgreSQL', 'Microsoft SQL Server', 'Microsoft Access', 'Sybase', 'InstantDB', 'Informix', 'Paradox', 'Data Warehouse']
            pourcentage_tab1 = 0
            pourcentage_tab2 = 0
            pourcentage_tab3 = 0 
            pourcentage_tab4 = 0
            pourcentage_tab5 = 0
            pourcentage_tab6 = 0
            pourcentage_tab7 = 0
            cppt = 0
            str1_Competence = "" 
            for i in competences:
                competences[cppt] = competences[cppt].split("\n")
                for ele in competences[cppt]:  
                    str1_Competence += ele + ":"
                cppt += 1
            str1_Competence = str1_Competence.split(":")
            competences = str1_Competence
            for i in dev_web:
                if i in competences:
                    pourcentage_tab1 += 1;
            if pourcentage_tab1 > 0:
                pourcentage_tab1 = (pourcentage_tab1/len(dev_web))*100

            for i in dev_mobile:
                if i in competences:
                    pourcentage_tab2 += 1;
            if pourcentage_tab2 > 0:
                pourcentage_tab2 = (pourcentage_tab2/len(dev_mobile))*100

            for i in dev_desktop:
                if i in competences:
                    pourcentage_tab3 += 1;
            if pourcentage_tab3 > 0:
                pourcentage_tab3 = (pourcentage_tab3/len(dev_desktop))*100

            for i in GL:
                if i in competences:
                    pourcentage_tab4 += 1;
            if pourcentage_tab4 > 0:
                pourcentage_tab4 = (pourcentage_tab4/len(GL))*100

            for i in DS:
                if i in competences:
                    pourcentage_tab5 += 1;
            if pourcentage_tab5 > 0:
                pourcentage_tab5 = (pourcentage_tab5/len(DS))*100

            for i in langages:
                if i in competences:
                    pourcentage_tab6 += 1;
            if pourcentage_tab6 > 0:
                pourcentage_tab6 = (pourcentage_tab6/len(langages))*100

            for i in data_bases:
                if i in competences:
                    pourcentage_tab7 += 1;
            if pourcentage_tab7 > 0:
                pourcentage_tab7 = (pourcentage_tab7/len(data_bases))*100
        ### Twitter ###
        twitter_dict = twitter(twitter_name)
        Profile_Name = twitter_dict["Profile_Name"]
        if Profile_Name != "None":
            compter_twitter += 5
        User_Name = twitter_dict["User_Name"]
        if User_Name != "None":
            compter_twitter += 5
        Biographie = twitter_dict["Biographie"]
        if Biographie != "None":
            compter_twitter += 5
        Following = twitter_dict["Following"]
        if Following != "None":
            compter_twitter += 5
        Followers = twitter_dict["Followers"]
        if Followers != "None":
            compter_twitter += 5
            Followers = int(Followers)
            if Followers > 100:
                compter_twitter += 5
        tweets = twitter_dict["tweets"]
        if tweets != "None":
            compter_twitter += 20
            sentiments = analyze_sentiment_twitter(tweets)
            mylist = zip(tweets, sentiments)
        nom = request.session['nom']
        prenom = request.session['prenom'] 
        ville = request.session['ville'] 
        pays = request.session['pays'] 
        company = request.session['company']
        aboutMe = request.session['aboutMe']
        emailRec = request.session['emailRec']
        return render(request, 'recherche/candidat.html', locals())
    return HttpResponseRedirect('/')



