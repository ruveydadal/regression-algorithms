# regression-algorithms
Machine Learning-6

Bu proje, veri madenciliği ve makine öğrenimi yaklaşımlarını kullanarak bir maaş tahmini yapmak için farklı regresyon modellerini inceleyen bir Python kodu içerir. Aşağıda, kodun nasıl çalıştığını ve hangi modellerin kullanıldığını anlatan detayları bulabilirsiniz.

## Proje Açıklaması

Bu proje, bir "maaslaryeni.csv" adlı veri setini kullanarak maaş tahminleri yapmayı amaçlar. Veri setinde farklı değişkenler (örneğin, deneyim, eğitim, yaş) ile maaş arasındaki ilişkiyi incelemek için çeşitli regresyon modelleri kullanılmıştır.

## Gereksinimler

Bu kodun çalıştırılabilmesi için aşağıdaki kütüphanelere ihtiyaç vardır:

- numpy
- matplotlib
- pandas
- statsmodels
- scikit-learn

## Kodun İçeriği

1. Veri setinin okunması:
   - "maaslaryeni.csv" adlı veri seti okunur.

2. Lineer Regresyon:
   - sklearn kütüphanesi kullanılarak lineer regresyon modeli oluşturulur.
   - statsmodels kullanılarak bu modelin özet istatistikleri hesaplanır.
   - R-kare (R2) değeri hesaplanır.

3. Polinomal Regresyon:
   - sklearn.preprocessing kullanılarak veri seti polinomal bir forma dönüştürülür.
   - Yeniden lineer regresyon modeli oluşturulur.
   - İkinci bir özet istatistiği hesaplanır.
   - R-kare (R2) değeri hesaplanır.

4. Çoklu Doğrusal Regresyon:
   - Veriler ölçeklenir (standartlaştırılır).
   - Destek Vektör Regresyon (SVR) modeli oluşturulur.
   - Özet istatistiği hesaplanır.
   - R-kare (R2) değeri hesaplanır.

5. Karar Ağacı Regresyonu:
   - Karar ağacı regresyon modeli oluşturulur.
   - Özet istatistiği hesaplanır.
   - R-kare (R2) değeri hesaplanır.

6. Rassal Orman Regresyonu:
   - Rassal Orman Regresyon modeli oluşturulur.
   - Özet istatistiği hesaplanır.
   - R-kare (R2) değeri hesaplanır.

7. Sonuçlar ve Özet R2 Değerleri:
   - Tüm regresyon modellerinin sonuçları ve R-kare (R2) değerleri listelenir.

## Kullanım

Bu kod, bir Python ortamında çalıştırılabilir. Aşağıdaki adımları izleyin:

1. Python ve gerekli kütüphaneleri yükleyin.
2. "maaslaryeni.csv" adlı veri setini aynı dizine koyun veya kod içindeki veri seti yolunu güncelleyin.
3. Kodu çalıştırın.

## Dikkat Edilmesi Gerekenler

- Kod içindeki veri setinin dosya yolunu kontrol edin ve güncelleyin.
- Veri seti ve özelliklerine göre uygun regresyon modelini seçin.
- Sonuçları değerlendirirken R-kare (R2) değerlerini dikkate alın.
