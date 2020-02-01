import 'package:fciapp/models/user.dart';
import 'package:fciapp/screens/home/home.dart';
import 'authenticate/authenticate.dart';
import 'package:flutter/material.dart';
import 'package:provider/provider.dart';

class Wrapper extends StatelessWidget {
  @override
  Widget build(BuildContext context) {

    final user = Provider.of<User>(context);
    print(user);
    
    // return either the Home or Authenticate widget
    if(user == null){
      return Authenticate();
    }
    else{
      return Home();
    }
    
  }
}

// import 'package:flutter/material.dart';
// import 'package:fciapp/models/user.dart';
// import 'package:fciapp/screens/authenticate/authenticate.dart';
// // import 'package:fciapp/screens/home/home.dart';
// import 'package:provider/provider.dart';
// import 'package:fciapp/screens/home/home.dart';
// class Wrapper extends StatefulWidget {
//   @override
//   _WrapperState createState() => _WrapperState();
// }

// class _WrapperState extends State<Wrapper> {
//   @override
//   Widget build(BuildContext context) {

//     final user = Provider.of<User>(context);
//     print(user);
// //    return either home or authenticate widget
//     if(user == null)
//     {
//       return Authenticate();
//     }
//     else{
//       return Home();
//     }
//   }
// }
