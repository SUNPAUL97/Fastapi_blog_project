from datetime import datetime
from collections import defaultdict
def calculate_session_times(logs):
  fmt = "%Y-%m-%d %H:%M:%S"
  sessions = defaultdict(list)
  user_login_time = {}

  for log in logs:
    timestamp_str, user_id, action = [part.strip() for part in log.split(" - ",2)]
    timestamp = datetime.strptime(timestamp_str, fmt)

    if action == "login":
      user_login_time[user_id] = timestamp
    elif action == "logout":
      if user_id in user_login_time:
        duration = (timestamp - user_login_time[user_id]).total_seconds()
        sessions[user_id].append(duration)
        del user_login_time[user_id]
        # Ignore other actions (like "Upload")

        # If some users never logged out, ignore incomplete sessions
  total_time = {user: int(sum(times)) for user, times in sessions.items()}

  return total_time

logs = [
    "2025-09-01 10:15:20 - user_1 - login",
    "2025-09-01 10:16:05 - user_2 - login",
    "2025-09-01 10:20:15 - user_1 - upload",
    "2025-09-01 10:21:00 - user_1 - logout",
    "2025-09-01 10:25:30 - user_2 - upload",
    "2025-09-01 10:30:00 - user_2 - logout"
]
print(calculate_session_times(logs))



compliance = pd.read_sql_query("SELECT * FROM compliance", conn)
compliance['date'] = pd.to_datetime(compliance['date'])