import os
import requests
import json
import time

# 可以在这里填入你的集合数据，或者取消下方注释从文件读取
words_list = [
	{
		"english": "What about",
		"chinese": "……怎么样?(用于提出建议)",
		"tags": [
			"unit6",
			"p70"
		],
		"lastTested": 1769259423694
	}
]


def download_audios():
    # 定义保存路径
    base_dir = "mp3"
    if not os.path.exists(base_dir):
        os.makedirs(base_dir)

    # 用来存储映射关系的字典
    audio_map = {}

    # 简单的请求头，模拟浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/115.0.0.0 Safari/537.36"
    }

    print(f"开始处理 {len(words_list)} 个单词...")

    for item in words_list:
        english = item.get("english")
        if not english:
            continue

        # 构造文件名
        file_name = f"{english}.mp3"
        save_path = os.path.join(base_dir, file_name)
        
        # 检查文件是否已存在且大小大于0，避免重复下载
        if os.path.exists(save_path) and os.path.getsize(save_path) > 0:
            print(f"[跳过] {english} 已存在")
            audio_map[english] = file_name
            continue

        # 构造请求参数
        # 百度TTS接口参数: lan=语言, text=内容, spd=语速, source=web(有助于直接访问)
        url = "https://fanyi.baidu.com/gettts"
        params = {
            "lan": "en",
            "text": english,
            "spd": "3",
            "source": "web"
        }

        print(f"[下载] 正在请求: {english} ...")
        
        try:
            response = requests.get(url, params=params, headers=headers, timeout=10)
            
            if response.status_code == 200:
                # 写入文件
                with open(save_path, "wb") as f:
                    f.write(response.content)
                
                # 下载成功后记录到映射字典
                audio_map[english] = file_name

                # 礼貌性延时，防止请求过快被封 IP
                time.sleep(0.5)
            else:
                print(f"  -> 下载失败，状态码: {response.status_code}")
                
        except Exception as e:
            print(f"  -> 发生错误: {e}")

    # 保存最终的映射 JSON 文件
    output_json = "audio_map.json"
    with open(output_json, "w", encoding="utf-8") as f:
        json.dump(audio_map, f, ensure_ascii=False, indent=4)
    
    print("\n" + "="*30)
    print(f"处理完成！")
    print(f"MP3 保存目录: {os.path.abspath(base_dir)}")
    print(f"映射 JSON: {os.path.abspath(output_json)}")

if __name__ == "__main__":
    # 如果你想从外部 JSON 文件读取 start
    # try:
    #     with open('source_list.json', 'r', encoding='utf-8') as f:
    #         words_list = json.load(f)
    # except FileNotFoundError:
    #     print("未找到源文件，使用内置示例数据...")
    # 如果你想从外部 JSON 文件读取 end

    download_audios()
