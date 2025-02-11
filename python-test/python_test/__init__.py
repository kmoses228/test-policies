from werkzeug.exceptions import Conflict

try:
  print("hi")
except Conflict:
  print("no")
