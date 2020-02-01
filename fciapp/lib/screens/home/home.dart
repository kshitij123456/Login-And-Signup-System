// import 'package:flutter/material.dart';

// class Home extends StatefulWidget {
//   @override
//   _HomeState createState() => _HomeState();
// }

// class _HomeState extends State<Home> {
//   @override
//   Widget build(BuildContext context) {
//     return Container(
//       child: Text('home'),
//     );
//   }
// }
import 'package:fciapp/screens/silo/silo_data.dart';
import 'package:flutter/material.dart';
import 'package:fciapp/services/auth.dart';

class Home extends StatelessWidget {
final AuthService _auth  = AuthService();

  @override
  Widget build(BuildContext context) {
    return Scaffold (
      backgroundColor: Colors.blue[500],
      appBar: AppBar(
        title: Text('FCI HomeScreen'),
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
                        MaterialPageRoute(builder: (context) => SiloData()),
                      );                    // return SiloData();
                  } ,
                  child: ListTile(
                  title: Text("Silo Data"),
                  
                  
                ),
              )
          ],
        ),

      ),
    );
  }
}
