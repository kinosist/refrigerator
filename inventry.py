import ui



def onBtnAdd(sender):
	#ds = ui.ListDataSource([1,2,3,4,5])
	#tableview1.data_source = ds
	#items = [{'title': 'test1'}, {'title': 'test2'}]
	#listdata = ui.ListDataSource('')
	#listdata.items = items
	#tableview1.data_source = listdata
	#tableview1.reload_data()
	#tableview1.insert(1, 'tesrs')
	
	ds = ui.ListDataSource([1,2,3,4,5])
	tv = ui.TableView()
	tv.data_source = ds
	tv.x = 130
	tv.y = 200
	v.add_subview(tv)
	



v = ui.load_view()
inventName = v['inventName']
datepicker = ['datepicker']
btnAdd = v['btnAdd']
tableview1 = ['tableview1']
tableview2 = ['tableview2']
v.present('sheet')
