# @Time         : 19-2-13 下午7:11
# @Author       : DioMryang
# @File         : dio.py
# @Description  :
import uuid

script = """
// overwrite the `languages` property to use a custom getter
Object.defineProperty(navigator, "languages", {
  get: function() {
    return ["zh-CN","zh","zh-TW","en-US","en"];
  }
});

// Overwrite the `plugins` property to use a custom getter.
Object.defineProperty(navigator, 'plugins', {
  get: () => [1, 2, 3, 4, 5],
});

// Pass the Webdriver test  
Object.defineProperty(navigator, 'webdriver', {
  get: () => false,
});


// Pass the Chrome Test.
// We can mock this in as much depth as we need for the test.
window.navigator.chrome = {
  runtime: {},
  // etc.
};

// Pass the Permissions Test.
const originalQuery = window.navigator.permissions.query;
window.navigator.permissions.query = (parameters) => (
  parameters.name === 'notifications' ?
    Promise.resolve({ state: Notification.permission }) :
    originalQuery(parameters)
);
"""


def response(flow):
    if "verify.meituan.com/v2" in flow.request.url :
        print("喵喵喵")
        a, b = flow.response.text.split("<meta charset=\"utf-8\">")

        flow.response.set_text(a + """<script>{}</script>""".format(script) + b)
        # text = "miaomiaomiao"
    # url = 'https://verify.meituan.com/v2/captcha'
    # if flow.request.url.startswith(url):
    #     file = open("miao-{}.jpeg".format(uuid.uuid4().__str__()), "wb")
    #     file.write(flow.response.content)
    #     file.close()