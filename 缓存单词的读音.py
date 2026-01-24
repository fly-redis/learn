import os
import requests
import json
import time

# 可以在这里填入你的集合数据，或者取消下方注释从文件读取
words_list = [
  {
    "english": "hello",
    "chinese": "你好",
  },
  {
    "english": "miss",
    "chinese": "女士",
  },
  {
    "english": "what",
    "chinese": "什么",
  },
  {
    "english": "is",
    "chinese": "是",
  },
  {
    "english": "what's",
    "chinese": "什么是",
  },
  {
    "english": "your",
    "chinese": "你的",
  },
  {
    "english": "name",
    "chinese": "名字",
  },
  {
    "english": "stand up",
    "chinese": "站起来",
  },
  {
    "english": "boy",
    "chinese": "男孩",
  },
  {
    "english": "and",
    "chinese": "和",
  },
  {
    "english": "girl",
    "chinese": "女孩",
  },
  {
    "english": "sit down",
    "chinese": "坐下",
  },
  {
    "english": "mr",
    "chinese": "先生",
  },
  {
    "english": "dad",
    "chinese": "爸爸",
  },
  {
    "english": "good morning",
    "chinese": "早上好",
  },
  {
    "english": "good afternoon",
    "chinese": "下午好",
  },
  {
    "english": "good evening",
    "chinese": "晚上好",
  },
  {
    "english": "goodbye",
    "chinese": "再见",
  },
  {
    "english": "good night",
    "chinese": "晚安",
  },
  {
    "english": "bye",
    "chinese": "再见",
  },
  {
    "english": "pencil",
    "chinese": "铅笔",
  },
  {
    "english": "sharpener",
    "chinese": "削笔刀",
  },
  {
    "english": "pencil box",
    "chinese": "铅笔盒",
  },
  {
    "english": "hi",
    "chinese": "你好",
  },
  {
    "english": "i",
    "chinese": "我",
  },
  {
    "english": "am",
    "chinese": "是",
  },
  {
    "english": "i'm",
    "chinese": "我是",
  },
  {
    "english": "schoolbag",
    "chinese": "书包",
  },
  {
    "english": "eraser",
    "chinese": "橡皮擦",
  },
  {
    "english": "crayon",
    "chinese": "蜡笔",
  },
  {
    "english": "pen",
    "chinese": "钢笔",
  },
  {
    "english": "ruler",
    "chinese": "尺子",
  },
  {
    "english": "look",
    "chinese": "看",
  },
  {
    "english": "have",
    "chinese": "有",
  },
  {
    "english": "a",
    "chinese": "一个",
  },
  {
    "english": "new",
    "chinese": "新的",
  },
  {
    "english": "it",
    "chinese": "它",
  },
  {
    "english": "it's",
    "chinese": "它是",
  },
  {
    "english": "nice",
    "chinese": "很好",
  },
  {
    "english": "can",
    "chinese": "可以",
  },
  {
    "english": "use",
    "chinese": "使用",
  },
  {
    "english": "find",
    "chinese": "找到",
  },
  {
    "english": "my",
    "chinese": "我的",
  },
  {
    "english": "sure",
    "chinese": "当然",
  },
  {
    "english": "hungry",
    "chinese": "饥饿的",
  },
  {
    "english": "dinner",
    "chinese": "晚餐",
  },
  {
    "english": "need",
    "chinese": "需要",
  },
  {
    "english": "vegetable",
    "chinese": "蔬菜",
  },
  {
    "english": "tomatoes with eggs",
    "chinese": "西红柿炒鸡蛋",
  },
  {
    "english": "What about",
    "chinese": "怎么样？",
  },
  {
    "english": "big",
    "chinese": "大的",
  },
  {
    "english": "small",
    "chinese": "小的",
  },
  {
    "english": "tall",
    "chinese": "高的",
  },
  {
    "english": "let's",
    "chinese": "让我们",
  },
  {
    "english": "OK",
    "chinese": "好的",
  },
  {
    "english": "his",
    "chinese": "他的",
  },
  {
    "english": "he",
    "chinese": "他",
  },
  {
    "english": "or",
    "chinese": "或者",
  },
  {
    "english": "her",
    "chinese": "她的",
  },
  {
    "english": "are",
    "chinese": "是",
  },
  {
    "english": "some",
    "chinese": "一些",
  },
  {
    "english": "too",
    "chinese": "也",
  },
  {
    "english": "tomorrow",
    "chinese": "明天",
  },
  {
    "english": "like",
    "chinese": "喜欢",
  },
  {
    "english": "yes",
    "chinese": "是的",
  },
  {
    "english": "no",
    "chinese": "不",
  },
  {
    "english": "want",
    "chinese": "想要",
  },
  {
    "english": "make",
    "chinese": "制作",
  },
  {
    "english": "say",
    "chinese": "说",
  },
  {
    "english": "ice cream",
    "chinese": "冰淇淋",
  },
  {
    "english": "candy",
    "chinese": "糖果",
  },
  {
    "english": "they",
    "chinese": "他们",
  },
  {
    "english": "bad",
    "chinese": "坏的",
  },
  {
    "english": "milk",
    "chinese": "牛奶",
  },
  {
    "english": "water",
    "chinese": "水",
  },
  {
    "english": "tea",
    "chinese": "茶",
  },
  {
    "english": "juice",
    "chinese": "果汁",
  },
  {
    "english": "cola",
    "chinese": "可乐",
  },
  {
    "english": "apple",
    "chinese": "苹果",
  },
  {
    "english": "banana",
    "chinese": "香蕉",
  },
  {
    "english": "orange",
    "chinese": "橙子",
  },
  {
    "english": "grape",
    "chinese": "葡萄",
  },
  {
    "english": "lemon",
    "chinese": "柠檬",
  },
  {
    "english": "drink",
    "chinese": "喝；饮料",
  },
  {
    "english": "fruit",
    "chinese": "水果",
  },
  {
    "english": "buy",
    "chinese": "买",
  },
  {
    "english": "cake",
    "chinese": "蛋糕",
  },
  {
    "english": "bread",
    "chinese": "面包",
  },
  {
    "english": "rice",
    "chinese": "米饭",
  },
  {
    "english": "noodle",
    "chinese": "面条",
  },
  {
    "english": "soup",
    "chinese": "汤",
  },
  {
    "english": "egg",
    "chinese": "鸡蛋",
  },
  {
    "english": "chicken",
    "chinese": "鸡肉",
  },
  {
    "english": "fish",
    "chinese": "鱼",
  },
  {
    "english": "tomato",
    "chinese": "西红柿",
  },
  {
    "english": "potato",
    "chinese": "土豆",
  },
  {
    "english": "food",
    "chinese": "食物",
  },
  {
    "english": "you",
    "chinese": "你",
  },
  {
    "english": "sorry",
    "chinese": "对不起",
  },
  {
    "english": "don't",
    "chinese": "不要",
  },
  {
    "english": "Here you are.",
    "chinese": "给你。",
  },
  {
    "english": "Thank you!",
    "chinese": "谢谢你！",
  },
  {
    "english": "You're welcome!",
    "chinese": "不客气！",
  },
  {
    "english": "ball",
    "chinese": "球",
  },
  {
    "english": "doll",
    "chinese": "玩偶",
  },
  {
    "english": "kite",
    "chinese": "风筝",
  },
  {
    "english": "jigsaw",
    "chinese": "拼图",
  },
  {
    "english": "toy",
    "chinese": "玩具",
  },
  {
    "english": "cat",
    "chinese": "猫",
  },
  {
    "english": "dog",
    "chinese": "狗",
  },
  {
    "english": "bike",
    "chinese": "自行车",
  },
  {
    "english": "bus",
    "chinese": "公交车",
  },
  {
    "english": "this",
    "chinese": "这个",
  },
  {
    "english": "mum",
    "chinese": "妈妈",
  },
  {
    "english": "gift",
    "chinese": "礼物",
  },
  {
    "english": "for",
    "chinese": "为了",
  },
  {
    "english": "so",
    "chinese": "如此",
  },
  {
    "english": "cute",
    "chinese": "可爱的",
  },
  {
    "english": "play with",
    "chinese": "和…… 一起玩",
  },
  {
    "english": "good",
    "chinese": "好的",
  },
  {
    "english": "friend",
    "chinese": "朋友",
  },
  {
    "english": "she",
    "chinese": "她",
  },
  {
    "english": "has",
    "chinese": "有",
  },
  {
    "english": "often",
    "chinese": "经常",
  },
  {
    "english": "share",
    "chinese": "分享",
  },
  {
    "english": "Happy birthday!",
    "chinese": "生日快乐！",
  },
  {
    "english": "face",
    "chinese": "脸",
  },
  {
    "english": "hair",
    "chinese": "头发",
  },
  {
    "english": "eye",
    "chinese": "眼睛",
  },
  {
    "english": "ear",
    "chinese": "耳朵",
  },
  {
    "english": "nose",
    "chinese": "鼻子",
  },
  {
    "english": "mouth",
    "chinese": "嘴巴",
  },
  {
    "english": "long",
    "chinese": "长的",
  },
  {
    "english": "short",
    "chinese": "短的",
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
