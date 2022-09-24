class StdoutRedirector(object):
    def __init__(self, text_widget):
        self.text_widget = text_widget 
 
    def write(self, s):
        self.text_widget.insert('end', s) # insert at end
        self.text_widget.see('end') # scroll to end

    def flush(self):
        pass