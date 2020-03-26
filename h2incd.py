import sys, time
from daemon import Daemon
from watchdog.observers import Observer
from watchdog.events import FileSystemEventHandler

class h2incDaemon(Daemon):
	def run(self):
		event_handler = MyHandler()
		observer = Observer()
		observer.schedule(event_handler, path='/usr/include', recursive=False)
		observer.start()
		try:
			while True:
				time.sleep(1)
		except KeyboardInterrupt:
			observer.stop()
		observer.join()

class MyHandler(FileSystemEventHandler):
    def on_modified(self, event):
        print(f'event type: {event.event_type}  path : {event.src_path}')

if __name__ == "__main__":
	daemon = h2incDaemon('/tmp/h2inc-daemon.pid')
	if len(sys.argv) == 2:
		if 'start' == sys.argv[1]:
			daemon.start()
		elif 'stop' == sys.argv[1]:
			daemon.stop()
		elif 'restart' == sys.argv[1]:
			daemon.restart()
		else:
			print('Unknown command')
			sys.exit(2)
		sys.exit(0)
	else:
		print('usage: %s start|stop|restart' % sys.argv[0])
		sys.exit(2)