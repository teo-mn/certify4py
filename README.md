# Certify4py 
Certify4py нь цахим сертификат, дипломыг блокчэйн дээр
баталгаажуулж өгөх https://github.com/teo-mn/certify-sc ухаалаг гэрээтэй харьцдаг python хэлний сан юм.
Уг ухаалаг гэрээ нь ИДС-ын дипломыг блокчэйнд баталгаажуулах стандарт бөгөөд дэлгэрэнгүйг дээрх линкээс харна уу.

Ингэхдээ https://chainpoint.org/ ийн v2.0 стандартыг ашигласан.

- Тестнет -тэй холбогдох нөүд: `https://node-testnet.corexchain.io`
- Теснет дээрх ухаалаг гэрээний хаяг: `0xc0668aC1BE4393F9dA6c8eB81a24faA4F9B04Edb`


- Майннет -тэй холбогдох нөүд: `https://node.corexchain.io`
- Майннет дээрх ухаалаг гэрээний хаяг: `0xD882B76106d0Ba1a54DE30d620dC5c2892Ae1677`


## Суулгах заавар
`pip install certify4py`

## Функцүүд
### `UniversityDiplomaIssuer.issue_pdf`
PDF файлын хаш утгыг тооцож ухаалаг гэрээнд бичээд,
гүйлгээний мэдээлэл болон нэмэлт мэдээллүүдийг файлын мэтадата дээр нэмэн шинэ файлд хадгална.

Байгуулагчийн параметр:

| Параметр                   | Тайлбар                               | Заавал эсэх |
|----------------------------|---------------------------------------|-------------|
| `certify_contract_address` | Ухаалаг гэрээний хаяг                 | тийм        |
| `node_host`                | Гүйлгээ хийх блокчэйний нөүдний хаяг  | тийм        |
| `issuer_address`           | Баталгаажуулагчийн хаяг               | тийм        |
| `issuer_name`              | Баталгаажуулагчийн нэр                | тийм        |
| `chain_id`                 | Баталгаажуулагчийн нэр (default=1104) | үгүй        |
| `hash_type`                | Хашийн төрөл (default=sha256)         | үгүй        |

`issue_pdf` функцийн параметр:

| Параметр                   | Тайлбар                               | Заавал эсэх                                     |
|----------------------------|---------------------------------------|-------------------------------------------------|
| `id`                       | Файлын ID                             | тийм                                            |
| `source_file_path`         | PDF эх файлын зам                     | тийм                                            |
| `destination_file_path`    | Мэтадата бичсэн PDF-ийг хадгалах зам  | тийм                                            |
 | `meta_data`                | Дипломын тухай мэдээлэл               | тийм                                            |
| `expire_date`              | Дуусах хугацаа                        | үгүй                                            |
| `desc`                     | Тайлбар, нэмэлт мэдээлэл              | үгүй                                            |
| `additional_info`          | Мэтадата дээр орох нэмэлт мэдээлэл    | үгүй                                            |
| `private_key`              | Баталгаажуулагчийн хувийн түлхүүр     | үгүй /key_store, passphrase өгөөгүй бол заавал/ |
| `key_store`                | Хувийн түлхүүрийн keystore файл       | үгүй /private_key өгөөгүй бол заавал/           |
| `passphrase`               | Хувийн түлхүүрийн passphrase файл     | үгүй /private_key өгөөгүй бол заавал/           |


#### Жишээ
```python
from certify4py.UniversityDiplomaIssuer import UniversityDiplomaIssuer

issuer = UniversityDiplomaIssuer(certify_contract_address,
                  node_host,
                  issuer_address,
                  issuer_name,
                  chain_id=3305)

try:
   txid, error = issuer.issue_pdf(
            id,
            source_file_path,
            destination_file_path,
            expire_date,
            desc,
            additional_info,
            private_key,
            key_store,
            passphrase) 
    if error is not None:
        print("Error: {}", error)
    else
        print("Success: {}", txid)
except Exception as e:
    print("Error: {}", e)
```
### `UniversityDiplomaIssuer.verify_pdf`
Блочкэйн дээр хадгалагдсан PDF файлийг шалгах.

Байгуулагчийн параметр:

| Параметр                   | Тайлбар                                    | Заавал эсэх |
|----------------------------|--------------------------------------------|-------------|
| `certify_contract_address` | Ухаалаг гэрээний хаяг                      | тийм        |
| `node_host`                | Гүйлгээ хийх блокчэйний нөүдний хаяг       | тийм        |

`UniversityDiplomaIssuer.verify_pdf` функцийн параметр:

| Параметр    | Тайлбар                  | Заавал эсэх                                    |
|-------------|--------------------------|------------------------------------------------|
| `file_path` | Метадата -тай файлын зам | тийм                                           |


#### Жишээ
```python
from certify4py.UniversityDiplomaIssuer import UniversityDiplomaIssuer

issuer = UniversityDiplomaIssuer(certify_contract_address,
                  teo_node_url,
                  chain_id=3305)

try:
    result = issuer.verify_pdf(file_path) 
    print("Result: {}", result)
except Exception as e:
    print("Error: {}", e)
```

### `Revoke`
Нэгэнт ухаалаг гэрээнд баталгаажсан PDF файлыг буцаан хүчингүй болгох функц

Байгуулагчийн параметр:

| Параметр                   | Тайлбар                                    | Заавал эсэх |
|----------------------------|--------------------------------------------|-------------|
| `certify_contract_address` | Ухаалаг гэрээний хаяг                      | тийм        |
| `node_host`                | Гүйлгээ хийх блокчэйний нөүдний хаяг       | тийм        |
| `issuer_address`           | Баталгаажуулагчийн хаяг                    | тийм        |
| `issuer_name`              | Баталгаажуулагчийн нэр                     | үгүй        |
| `chain_id`                 | Баталгаажуулагчийн нэр                     | үгүй        |
| `hash_type`                | Хашийн төрөл                               | үгүй        |


`revoke` функцийн параметр:

| Параметр       | Тайлбар                           | Заавал эсэх                                     |
|----------------|-----------------------------------|-------------------------------------------------|
| `file_path`    | Мэтадата бичигдсэн PDF файлын зам | тийм                                            |
| `revoker_name` | Хүчингүй болгож буй хүний нэр     | тийм                                            |
| `private_key`  | Баталгаажуулагчийн хувийн түлхүүр | үгүй /key_store, passphrase өгөөгүй бол заавал/ |
| `key_store`    | Хувийн түлхүүрийн key_store файл  | үгүй /private_key өгөөгүй бол заавал/           |
| `passphrase`   | Хувийн түлхүүрийн passphrase файл | үгүй /private_key өгөөгүй бол заавал/           |

#### Жишээ
```python
from certify4py.UniversityDiplomaIssuer import PdfIssuer

issuer = PdfIssuer(certify_contract_address,
                  node_host,
                  issuer_address,
                  issuer_name,
                  chain_id=3305)
try:
    txid, error = issuer.revoke(file_path,
                              revoker_name,
                              key_store,
                              passphrase)
    print("Txid: {}", txid)
except Exception as e:
    print("Error: {}", e)  
```
