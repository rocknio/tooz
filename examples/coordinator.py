from tooz import coordination

coordinator = coordination.get_coordinator(('memcached://192.168.1.200:31000', 'memcached://192.168.1.200:32000', 'memcached://192.168.1.200:30000'), b'host-1')
# coordinator = coordination.get_coordinator('memcached://192.168.1.200:31000', b'host-1')

coordinator.start()
coordinator.stop()
