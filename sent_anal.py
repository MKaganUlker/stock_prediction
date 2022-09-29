from textblob import TextBlob
from googletrans import Translator, constants
from transformers import AutoModelForSequenceClassification, AutoTokenizer, pipeline

positive_words = ["genişleme","geliştirme","destek","katkı"]
negative_words = ["batık","batma",""]

#turkish article translation for potentially use readymade english sentiment analysis models
translator = Translator()
turk_new="İSTANBUL (AA) - Akbank’ın İnovasyon Merkezi olan Akbank LAB, 2016 yılından beri kurum içi girişimcilik ve inovasyon programlarını genişletmeye ve geliştirmeye devam ediyor.Akbank'tan yapılan açıklamaya göre, finteklerle yapılan iş birlikleri, yürütülen projeler ve açık inovasyon programlarıyla bu kültürü destekleyen Akbank, bu yeni program ile kendi girişimlerini kurmak isteyen çalışanlarını desteklemeyi, birlikte çalışacağı iş ortaklarını kurum içerisinden çıkarmayı ve Türkiye’deki girişimcilik ekosistemini daha da geliştirmeyi amaçlıyor.Akbanklıların girişim fikirleri üzerinde tam zamanlı olarak çalışabilmesine olanak sağlayan ve bu anlamda Türkiye’de bir ilk olan Akbank+ Programı’na şirkete yeni katılan veya yıllardır Akbank’ta çalışan tüm Akbanklılar başvurabilecek.Açıklamada görüşlerine yer verilen Akbank Bireysel Bankacılık ve Dijital Çözümler Genel Müdür Yardımcısı Burcu Civelek Yüce, Akbank+ Programı’na ölçeklenebilir iş fikirleriyle başvuru yapan Akbanklılar arasından seçilenlerin tam zamanlı olarak iş fikirlerine odaklanacaklarını kaydetti.Yüce, çeşitli eğitimlere, atölyelere ve yoğun mentorluk seanslarına katıldıktan sonra kuluçka aşamasında fikirlerini geliştireceklerini belirterek, 'Tasarım ve ürün geliştirme aşamalarına ilerleyecekler. Akbank+ Yatırım Komitesi’nin vereceği karar doğrultusunda girişimlere Akbank olarak yatırım yapacağız ve çalışma arkadaşlarımızın şirketlerini kurmalarını sağlayacağız.Yatırım alamayan ekipler ise edindikleri girişimcilik ve inovasyon yetkinliklerini yeni projelerde kullanmak üzere İnovasyon Elçisi rolüyle Akbank’taki işlerine dönecek ve bu yolculuğa çıkacak diğer Akbanklılara rehberlik edecekler. Akbank+’ı alanında tecrübeli kurumlar ve mentorların desteği ile yürütüyoruz. Alanında bir ilk olacak bu programın hem Bankamız hem de ülkemiz girişimcilik ekosistemine önemli katkılar sunacağına inanıyoruz.” açıklamasında bulundu.Akbank İnsan ve Kültür Genel Müdür Yardımcısı Pınar Anapa ise 'Akbank’ı geleceğe taşıyacak fikirlerin geliştirilmesi ve desteklenmesi, aynı zamanda banka içinde inovasyon ve girişimcilik kültürünün yaygınlaştırılması için yürüttüğümüz programları Akbank+ ile bir adım ileriye taşıyoruz.Akbank+ Programı’nın kurum içinde girişimcilik ve inovasyon yetkinliklerinin geliştirilmesi ve bu ruhun yaygınlaştırılması anlamında da önemli katkılar sağlayacağını düşünüyoruz. Bu programa katılan arkadaşlarımız aynı zamanda birer kültür elçisi olacaklar. Akbank+ ile merkezinde insan olan strateji ve uygulamalarımıza bir yenisini ekliyor, kariyer yolculuğunda zaman ve mekân bağımsız olarak yanındayız diyoruz.' yorumunu yaptı."
translation = translator.translate(turk_new)

#general turkish sentiment analysis for 
model = AutoModelForSequenceClassification.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
tokenizer = AutoTokenizer.from_pretrained("savasy/bert-base-turkish-sentiment-cased")
sa= pipeline("sentiment-analysis", tokenizer=tokenizer, model=model)

p = sa("Akbank, Akbanklıların kendi girişimlerini kurmasını destekliyor")
print(p)
# [{'label': 'LABEL_1', 'score': 0.9871089}]
print(p[0]['label'] == 'negative')
# True

p2 = sa("Akbank’ta teknik sorun")
print(p2)
# [{'label': 'LABEL_1', 'score': 0.9871089}]
print(p2[0]['label'] == 'positive')
# True")




#print(f"{translation.origin} ({translation.src}) --> {translation.text} ({translation.dest})")

feedback1 = "ISTANBUL (AA) - Akbank LAB, Akbank's Innovation Center, has been expanding and developing its in-house entrepreneurship and innovation programs since 2016.Supporting this culture with collaborations with fintechs, projects carried out and open innovation programs, Akbank aims to support its employees who want to establish their own ventures, to remove business partners from the institution and to further develop the entrepreneurship ecosystem in Turkey with this new program. aims.All Akbankers who have recently joined the company or have been working at Akbank for years can apply to the Akbank+ Program, which is a first in Turkey and allows Akbank employees to work on their entrepreneurial ideas full-time.Burcu Civelek Yüce, Deputy General Manager of Akbank Retail Banking and Digital Solutions, whose views are included in the statement, noted that those selected among Akbankers who applied to the Akbank+ Program with scalable business ideas will focus on their business ideas full-time.Yüce, stated that they will develop their ideas during the incubation phase after participating in various trainings, workshops and intensive mentoring sessions, 'They will progress to the design and product development stages. In line with the decision of the Akbank+ Investment Committee, we will invest in startups as Akbank and enable our colleagues to establish their companies.Teams that cannot receive investment will return to their jobs at Akbank as Innovation Ambassadors to use their acquired entrepreneurship and innovation competencies in new projects and will guide other Akbank employees on this journey. We run Akbank+ with the support of experienced institutions and mentors. We believe that this program, which will be a first in its field, will make significant contributions to the entrepreneurship ecosystem of both our Bank and our country.” made a statement.Akbank Human and Culture Deputy General Manager Pınar Anapa said: “With Akbank+, we are taking our programs one step further with the aim of developing and supporting ideas that will carry Akbank into the future, as well as spreading the innovation and entrepreneurship culture within the bank.We believe that the Akbank+ Program will also make significant contributions to the development of entrepreneurship and innovation competencies within the organization and to the dissemination of this spirit. Our friends participating in this program will also be cultural ambassadors. With Akbank+, we are adding a new one to our human-centered strategies and practices, and we say that we are with you in your career journey regardless of time and place.' made his comment."

blob1 = TextBlob(translation.text)


#print(blob1.sentiment)