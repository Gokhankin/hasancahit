import os

html_path = 'gelecegi-yakala-son.html'
out_path = 'gelecegi-yakala-son.html'

with open(html_path, 'r', encoding='utf-8') as f:
    text = f.read()

replacements = {
    "Yaşadığımız yılları birlikte geçirmek bize ne büyük şanstır! Hayatındaki doğru kişilerin yanında olmayı istiyorum, çünkü senin gibi bir arkadaşı olmak,":
    "Yaşadığımız yılları birlikte geçirmek bizim için ne büyük şanstır! Hayatındaki doğru kişilerin yanında olmak istiyorum, çünkü senin gibi bir arkadaşa sahip olmak,",
    
    "güleryüzünle": "güler yüzünle",
    
    "orada olacağını bilmek bana hep iyi geliyor. Bu arkadaşlık benim için çok değerli. Nice yaşlara, nice anılara. İyi ki varsın":
    "orada olacağını bilmek bana hep iyi geliyor. Bu arkadaşlık benim için çok değerli. Nice yaşlara, nice anılara. İyi ki varsın.",
    
    "Antalyanın gülü doğum günün kutlu olsun, nice mutlu ve sağlıklı senelerine.": 
    "Antalya'nın gülü, doğum günün kutlu olsun, nice mutlu ve sağlıklı senelerine.",

    "Hasan Cahit doğduğun gün dün gibi aklımda,":
    "Hasan Cahit, doğduğun gün dün gibi aklımda;",

    "karşılaş sağlıklı huzurlu": "karşılaş, sağlıklı ve huzurlu",

    "Hasan iyi ki varsın yeni yaşında her şey gönlünce olsun nice mutlu yaşlara kanka🥳🎂✨":
    "Hasan, iyi ki varsın. Yeni yaşında her şey gönlünce olsun, nice mutlu yaşlara kanka! 🥳🎂✨",
    
    "Sevgili Hasan Cahit, Doğum Günün Kutlu Olsun.":
    "Sevgili Hasan Cahit, doğum günün kutlu olsun.",
    
    "ailene milletimize devletimize": "ailene, milletimize, devletimize",

    "Sevgili HasanCahit, Yeni yaşında Üniversite hayatını tamamlamış, İş Dünyasına adımını atmış, Modern Türkiyenin gelişimi için çalışmalara başlamış, Bir gün başkanlığını yapacağına inandığım Antalyaspor umuzun Süperlig de devam ettiği, Büyüklüğünü Şampiyonlukla taçlandırmış bir Fenerbahçenin olduğu bir yıl yaşamanı gönülden istiyorum Sana Ailen ve sevdiklerinle beraber her şeyin gönlünce olacağı sağlık ve sevgi dolu yıllar diliyorum. İyiki doğdun hayatımıza girdin Doğum Günün kutlu olsun Evlat.":
    "Sevgili Hasan Cahit, yeni yaşında üniversite hayatını tamamlamış, iş dünyasına adımını atmış, modern Türkiye'nin gelişimi için çalışmalara başlamış olmanı diliyorum. Bir gün başkanlığını yapacağına inandığım Antalyaspor'umuzun Süper Lig'de başarıyla yoluna devam ettiği, büyüklüğünü şampiyonlukla taçlandırmış bir Fenerbahçe'nin olduğu bir yıl yaşamanı gönülden arzuluyorum. Sana ailen ve sevdiklerinle beraber her şeyin gönlünce olacağı, sağlık ve sevgi dolu yıllar diliyorum. İyi ki doğdun, hayatımıza girdin. Doğum günün kutlu olsun evlat.",

    "Londrada": "Londra'da",
    "birbirimiziniz": "birbirimizin",
    
    "Az adam var, sende onlardansın. İyi ki doğdun , nice beraber yaşlara":
    "Az adam var, sen de onlardansın. İyi ki doğdun, nice beraber yaşlara.",
    
    "Canım Hasan Cahidim daha bize dün gibi geliyor büyüdün Unuversiteli oldun bitiriyorsun ne mutlu bize. Çocukluğumdan beri hep saygılı sevecen mutlu bir çocuk oldun inşallah bütün ömrün boyunca mutlu olursun. Doğum günün kutlu olsun Nice mutlu yıllar seninle olsun. Seni çok seven Feral teyzen.":
    "Canım Hasan Cahit'im, bize daha dün gibi gelse de büyüdün, üniversiteli oldun ve bitiriyorsun. Ne mutlu bize! Çocukluğundan beri hep saygılı, sevecen ve mutlu bir çocuk oldun. İnşallah bütün ömrün boyunca hep böyle mutlu olursun. Doğum günün kutlu olsun. Nice mutlu yıllar seninle olsun. Seni çok seven Feral teyzen.",
    
    "Sevgili Hasancahit,": "Sevgili Hasan Cahit,",
    "başarılı bir gençsin, son görüştüğümüzde": "başarılı bir gençsin; son görüştüğümüzde",
    "başarısında gelecekte": "başarısı da gelecekte",
    "herşey": "her şey",
    
    "olgunluk...sorumluluk ve ince espri zekası ile tereddütsüz arkadaşım oldu..Bugünlerde de bütün bu niteliklerinin bilincinde olan ve bunları geliştirmeye odaklanmış Hasan Cahit i gözlemliyorum..Kardeş.. Nice":
    "olgunluk, sorumluluk ve ince espri zekâsı ile tereddütsüz çok iyi bir arkadaşım oldu... Bugünlerde de bütün bu niteliklerinin bilincinde olan ve bunları geliştirmeye odaklanmış Hasan Cahit'i gözlemliyorum... Kardeşim, nice",
    
    "Hasan Cahitcigim": "Hasan Cahitçiğim",
    "Annen ve Baban": "annen ve baban",

    "bağına sahip olan kişi denilince işte Hasan Cahit.": "bağına sahip olan kişi denilince akla gelen şey, işte Hasan Cahit.",

    "Seni çok seviyoruzz🤍🤍🤍": "Seni çok seviyoruz. 🤍🤍🤍",

    "sevdiklerinle yılların olsun.": "sevdiklerinle nice yılların olsun.",
    
    "çokk ": "çok ",

    "6 seneye yakindir samimi arkadasiz. Pek çok unutulmayacak güzel anılar biriktirdik. İyi ki varsin, seviliyorsun. Nice mutlu yaşların olsun, iyi ki tanismisiz.":
    "6 seneye yakındır samimi arkadaşız. Pek çok unutulmayacak güzel anı biriktirdik. İyi ki varsın, seviliyorsun. Nice mutlu yaşların olsun, iyi ki tanışmışız.",

    "değişsede": "değişse de",
    "olucağını": "olacağını",
    "Hasanım": "Hasan'ım",
    "başkanım,": "başkanım,",

    "Hasan Cahit'ciğim": "Hasan Cahitçiğim",

    "mutevaziligi": "mütevazılığı",
    "dogdun": "doğdun",
    "İyiki varsın iyiki dogdun.": "İyi ki varsın, iyi ki doğdun.",

    "Tac'nin": "TAC'nin",

    "Hasan Cahit Akıncıoğlu Dedemin Babamın ve Kardeşimin adlarını geleceğe taşıyan kıymetli temel taşısın Sevgili oğlum varlığınla asaletinle aldığın iyi eğitiminle her daim onurumuz gururumuzsun doğum gününü kutluyorum seni çok seviyor ve kocaman öpüyorum hayatında her konuda başarılar diliyorum":
    "Hasan Cahit Akıncıoğlu; dedemin, babamın ve kardeşimin adlarını geleceğe taşıyan kıymetli temel taşısın. Sevgili oğlum, varlığınla, asaletinle ve aldığın iyi eğitimle her daim onurumuz, gururumuzsun. Doğum gününü kutluyor, seni çok seviyor ve kocaman öpüyorum. Hayatında her konuda başarılar diliyorum.",

    "yürdüğün": "yürüdüğün",
    "Yarın öbürgün": "Yarın öbür gün",
    "gidicek": "gidecek",

    "iyisin iyisindir.": "iyisindir.",

    "Öncelikle Doğum Günün kutlu ve her şey gönlünce olsun.": "Öncelikle doğum gününün kutlu ve her şeyin gönlünce olmasını dilerim.",
    "Buda sana bağlıdır.": "Bu da sana bağlıdır.",
    "Sonrada Fenerbahçenin Şampiyonluğunu": "Sonra da Fenerbahçe'nin şampiyonluğunu"
}

for old, new in replacements.items():
    if old in text:
        text = text.replace(old, new)

with open(out_path, 'w', encoding='utf-8') as f:
    f.write(text)

print(f"Imla hataları düzeltildi. {out_path} olarak kaydedildi.")
