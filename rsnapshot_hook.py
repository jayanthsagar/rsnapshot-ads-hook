class rsnapshot_hook:
	"""A rsnapshot hook for ADS"""
#	lab = 'dummy.vlabs.ac.in'
#	backup_type = 'backup' #Type specifies whethe 'backup' or 'backup_script'
#	points = ['/var/','/root']
#	local_path = '.snapshots/' # local path on rsnapshot server to store backups

	def __init__(self):
		pass
        #self.add_backup(lab, backup_type, points, local_path)
		
	def add_backup(self, lab, backup_type, points, local_path):
		f = open('dummy.txt', 'aw')
		f.write("\n - name: "+lab)
		f.write("\n   points:")
		f.write('\n       - [backup_script, /bin/date "+ backup of '+lab+' started at %c" > start.txt, '+lab+'/'+lab+'_start]')
		for i in points:
			f.write('\n       - ['+backup_type+', root@'+lab+':'+i+', '+local_path+']')
		f.write('\n       - [backup_script, /bin/date "+ backup of '+lab+' stopped at %c" > stop.txt, '+lab+'/'+lab+'_stop]')
		f.close()

	def modify_backup(self, lab, backup_type, points, local_path):
		self.f.write()
	

	def remove_backup(self, lab, backup_type, points, local_path):
		self.f.write()


a = rsnapshot_hook()	
a.add_backup('b.vlabs.ac.in', 'backup', ['/root', '/home'], '/home')
