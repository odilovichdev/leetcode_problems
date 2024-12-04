# v1
# class BrowserHistory:
#
#     def __init__(self, homepage: str):
#         self.stack1 = [homepage]
#         self.stack2 = []
#
#     def visit(self, url: str) -> None:
#         self.stack1.append(url)
#         self.stack2.clear()
#
#     def back(self, steps: int) -> str:
#         for i in range(steps):
#             if 1 < len(self.stack1):
#                 self.stack2.append(self.stack1.pop())
#             else:
#                 break
#         return self.stack1[-1]
#
#     def forward(self, steps: int) -> str:
#         for i in range(steps):
#             if len(self.stack2):
#                 self.stack1.append(self.stack2.pop())
#             else:
#                 break
#         return self.stack1[-1]


class BrowserHistory:

    def __init__(self, homepage: str):
        self.history = [homepage]
        self.pos = 0

    def visit(self, url: str) -> None:
        self.pos += 1
        self.history = self.history[:self.pos]
        self.history.append(url)

    def back(self, steps: int) -> str:
        if self.pos > steps:
            self.pos -= steps
        else:
            self.pos = 0
        return self.history[self.pos]

    def forward(self, steps: int) -> str:
        if self.pos + steps < len(self.history):
            self.pos += steps
        else:
            self.pos = len(self.history) - 1
        return self.history[self.pos]












# Your BrowserHistory object will be instantiated and called as such:
# obj = BrowserHistory(homepage)
# obj.visit(url)
# param_2 = obj.back(steps)
# param_3 = obj.forward(steps)
# BrowserHistory browserHistory = new BrowserHistory("leetcode.com");
# browserHistory.visit("google.com");       // You are in "leetcode.com". Visit "google.com"
# browserHistory.visit("facebook.com");     // You are in "google.com". Visit "facebook.com"
# browserHistory.visit("youtube.com");      // You are in "facebook.com". Visit "youtube.com"
# browserHistory.back(1);                   // You are in "youtube.com", move back to "facebook.com" return "facebook.com"
# browserHistory.back(1);                   // You are in "facebook.com", move back to "google.com" return "google.com"
# browserHistory.forward(1);                // You are in "google.com", move forward to "facebook.com" return "facebook.com"
# browserHistory.visit("linkedin.com");     // You are in "facebook.com". Visit "linkedin.com"
# browserHistory.forward(2);                // You are in "linkedin.com", you cannot move forward any steps.
# browserHistory.back(2);                   // You are in "linkedin.com", move back two steps to "facebook.com" then to "google.com". return "google.com"
# browserHistory.back(7);                   // You are in "google.com", you can move back only one step to "leetcode.com". return "leetcode.com"
