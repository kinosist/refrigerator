import ui


def onBtnAdd(sender):
	
	name = sender.superview['inventName']
	
	datepicker = sender.superview['datepicker']
	print(datepicker.date)
	items = [str(datepicker.date) + ' ' + name.text]
	

	#items = [{'title': 'test1'}, {'title': 'test2'}]
	listdata = ui.ListDataSource('')
	listdata.items = items
	tableview = sender.superview['tableview1']
	tableview.data_source = listdata
	tableview.reload_data()
	#tableview1.data_source = listdata
	#tableview1.reload_data()
	#tableview1.insert(1, 'tesrs')
	
	#ds = ui.ListDataSource([1,2,3,4,5])
	#tv = ui.TableView()
	#tv.data_source = ds
	#tv.x = 130
	#tv.y = 200
	#v.add_subview(tv)
	



v = ui.load_view()
inventName = v['inventName']
datepicker = ['datepicker']
btnAdd = v['btnAdd']
tableview1 = ['tableview1']
tableview2 = ['tableview2']
v.present('sheet')
