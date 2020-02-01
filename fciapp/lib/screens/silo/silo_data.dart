import 'package:fciapp/screens/home/home.dart';
import 'package:flutter/material.dart';
import 'package:fciapp/services/auth.dart';
import 'package:http/http.dart' as http;
import 'package:url_launcher/url_launcher.dart';
// import 'advancedsilodata.dart';
import 'dart:convert';

import 'advancedsilodata.dart';

class SiloData extends StatelessWidget
{
	final AuthService _auth  = AuthService();
	Future<http.Response> fetchPost() {
		print(http.get('192.168.24.226:5000/silo_1'));
		return http.get('192.168.24.226:5000/silo_1');

	}
	
	
	// var silofakee = {"silo_details": {"silo_name": {"0": "silo_1"}, "silo_address": {"0": "a"}, "silo_district": {"0": "a"}, "silo_city": {"0": "a"}, "silo_state": {"0": "U. P."}, "lease_expiry": {"0": "2022-01-01"}, "contact_person_id": {"0": "person_1"}, "silo_type": {"0": "type c"}, "silo_ownership": {"0": "FCI"}}, "silo_storage": {"type_grain": {"0": "wheat", "1": "corn", "2": "maize"}, "capacity": {"0": "942", "1": "678", "2": "482"}, "silo_current_capacity": {"0": "563", "1": "0", "2": "331"}}};
	@override
	Widget build(BuildContext context) 
	{
		var silofake = {'name':'Silo A', 'grainstored': 'wheat','leaseexpiry': '10/5/2020', 'ownership':'FCI','contactname':'JKR',
													'email':'amoghdhardiwan@gmail.com','number' : '0123456789' };
			// List responseJson = json.decode(silofake.toString());
			// var rest = responseJson['articles'] as List;

		return Scaffold 
		(
							backgroundColor: Colors.blue[500],
							appBar: AppBar(
								title: Text('Silo Data'),
								backgroundColor: Colors.blue[200],
								elevation: 0.0,
								actions: <Widget>[
									FlatButton.icon(
										icon: Icon(Icons.person),
										label: Text('Logout'),
										onPressed: () async {
											await _auth.signOut();
										},
									)
								],
							),
							drawer: Drawer(
								child: Column(
									children: <Widget>[
										UserAccountsDrawerHeader(
											accountEmail: Text('example@email.com'),
											accountName: Text('John Doe'),
											currentAccountPicture: CircleAvatar(
												
											),
											
										),
										FlatButton(
													onPressed:() {
														Navigator.push(
																context,
																MaterialPageRoute(builder: (context) => Home()),
															);                    // return SiloData();
													} ,
													child: ListTile(
													title: Text("Home"),
													
													
												),
											)
									],
								),

							),
						body: Container
							(			color: Colors.white,
										child: Column(
											children: <Widget>[
												DataTable
													(	headingRowHeight: 0.0,
														columns: [DataColumn(label: Text(' ')),DataColumn(label: Text(' '))],
															rows: [
																DataRow(cells: [
																	DataCell(Text('Silo Name')),
																	DataCell(Text(silofake['name'])),
																]
																),
																DataRow(cells: [
																	DataCell(Text('Grain Stored')),
																	DataCell(Text(silofake['grainstored'])),
																]
																),
																DataRow(cells: [
																	DataCell(Text('Lease Expiry')),
																	DataCell(Text(silofake['leaseexpiry'])),
																]
																),
																DataRow(cells: [
																	DataCell(Text('Ownership')),
																	DataCell(Text(silofake['ownership'])),
																]
																),
																DataRow(cells: [
																	DataCell(Text('Contact Person')),
																	DataCell(
																		DataTable(
																			headingRowHeight: 0.0,
																			dataRowHeight: 17.0,
																			columns: [DataColumn(label: Text(' '))],
																			rows: [
																				DataRow(cells:
																				[DataCell(Text(silofake['contactname'])),]
																				),
																				DataRow(cells:
																				[DataCell(FlatButton(
																					onPressed: () {
																						launch("mailto:${silofake['email']}");
																					},
																					child:Text(silofake['email']),
																					),
																					
																					),]
																				),
																				DataRow(cells:[
																					DataCell(
																						FlatButton(
																						onPressed: () {
																							launch("tel:${silofake['number']}");
																						},
																						child:Text('Phone'),
																						),
																						),
																					]
																				)
																			],)
																	),
																]
																),
																// DataRow(cells:[
																// 	DataCell(Text('Silo Capacity')),
																// 	DataCell(LinearProgressIndicator())
																// ])
																] 
													),
														Align(
															alignment: FractionalOffset.bottomCenter,
															child:RaisedButton(
																	onPressed: () {
																		showModalBottomSheet(
																			context: context,
																			builder: (context) {
																				return Column(
																					children: <Widget>[
																						ListTile(
																							leading: Icon(Icons.settings),
																							title: Text('More Info'),
																							onTap: () => Navigator.push(
																														context,
																														MaterialPageRoute(builder: (context) => AdvancedSiloData()),
																													)
																						)
																					],
																				);
																			}
																		);
																	},
																	child:Center(child: ListTile(
															  	leading: Icon(Icons.more),
															  	title: Text('Options'),
															  )),
															)
														)
													],
										)
										
							// child: Text(responseJson.toString()),
							),
							
		);
		
	}
}
