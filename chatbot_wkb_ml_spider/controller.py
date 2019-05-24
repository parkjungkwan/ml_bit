import cgi
from chatbot_wkb_ml_spider.botengine import make_reply
form = cgi.FieldStorage()

class ChatbotController:
    def __init__(self):
        pass

    def main(self):
        m = form.getvalue("m", default="")
        if m == "":
            self.show_form()
        elif m == "say":
            self.api_say()

    # 사용자의 입력에 응답하기 --- (※3)
    def api_say(self):
        print("Content-Type: text/plain; charset=utf-8")
        print("")
        txt = form.getvalue("txt", default="")
        if txt == "": return
        res = make_reply(txt)
        print(res)

    # 입력 양식 출력하기 --- (※4)
    def show_form(self):
        print("Content-Type: text/html; charset=utf-8")
        print("")
        print("""
        <html><meta charset="utf-8"><body>
        <script src="https://code.jquery.com/jquery-3.1.1.min.js"></script>
        <style>
            h1   { background-color: #ffe0e0; }
            div  { padding:10px; }
            span { border-radius: 10px; background-color: #ffe0e0; padding:8px; }
            .bot { text-align: left; }
            .usr { text-align: right; }
        </style>
        <h1>대화하기</h1>
        <div id="chat"></div>
        <div class='usr'><input id="txt" size="40">
        <button onclick="say()">전송</button></div>
        <script>
        var url = "./chatbot.py";
        function say() {
          var txt = $('#txt').val();
          $.get(url, {"m":"say","txt":txt},
            function(res) {
              var html = "<div class='usr'><span>" + esc(txt) +
                "</span>: 나</div><div class='bot'> 봇:<span>" + 
                esc(res) + "</span></div>";
              $('#chat').html($('#chat').html()+html);
              $('#txt').val('').focus();
            });
        }
        function esc(s) {
            return s.replace('&', '&amp;').replace('<','&lt;')
                    .replace('>', '&gt;');
        }
        </script></body></html>
        """)