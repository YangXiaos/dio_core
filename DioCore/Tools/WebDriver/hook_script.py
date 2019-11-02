import mitmproxy
from mitmproxy import ctx


injected_javascript = '''
Object.defineProperty(navigator, "languages", {
  get: function() {
    return ["zh-CN","zh","zh-TW","en-US","en"];
  }
});
Object.defineProperty(navigator, 'plugins', {
  get: () => [1, 2, 3, 4, 5],
});
Object.defineProperty(navigator, 'webdriver', {
  get: () => false,
});window.navigator.chrome = {
  runtime: {},
  // etc.
};const originalQuery = window.navigator.permissions.query;window.navigator.permissions.query = (parameters) => (
  parameters.name === 'notifications' ?
    Promise.resolve({ state: Notification.permission }) :
    originalQuery(parameters)
);
'''


def response(flow: mitmproxy.http.HTTPFlow):

    if "fill_mobile.htm" in flow.request.url or "com/member/login.jhtml" in flow.request.url:
        html = flow.response.text
        html = html.replace('<head>', '<head><script>{}</script>'.format(injected_javascript))
        flow.response.text = str(html)
        ctx.log.info('>>>> js代码插入成功 <<<<')
