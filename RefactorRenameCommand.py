Hello, World!import sublime
import sublime_plugin

class RefactorRenameCommand(sublime_plugin.TextCommand):
  
  def run(self, edit, **args):
    self.view.insert(edit, 0, "Hello, World!")
