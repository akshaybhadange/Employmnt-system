import 'package:book_app/constants.dart';
import 'package:book_app/screens/details_screen.dart';
import 'package:book_app/widgets/book_rating.dart';
import 'package:book_app/widgets/reading_card_list.dart';
import 'package:book_app/widgets/two_side_rounded_button.dart';
import 'package:book_app/widgets/instructor_card.dart';

import 'package:flutter/material.dart';

class HomeScreen extends StatelessWidget {
  @override
  Widget build(BuildContext context) {
    var size = MediaQuery.of(context).size;
    return Scaffold(
      body: SingleChildScrollView(
        child: Column(
          crossAxisAlignment: CrossAxisAlignment.start,
          children: <Widget>[
            Container(
              width: double.infinity,
              decoration: BoxDecoration(
                image: DecorationImage(
                  image: AssetImage("assets/images/main_page_bg.png"),
                  alignment: Alignment.topCenter,
                  fit: BoxFit.fitWidth,
                ),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  SizedBox(height: size.height * .1),
                  Padding(
                    padding: const EdgeInsets.symmetric(horizontal: 24),
                    child: RichText(
                      text: TextSpan(
                        style: Theme.of(context).textTheme.bodyText1.apply(color: kBlackColor),
                        
                        children: [
                          TextSpan(
                              text: "DashBoard ",
                              style: TextStyle(
                                fontWeight: FontWeight.bold,
                                fontSize: 35
                              ))
                        ],
                      ),
                    ),
                  ),
                  SizedBox(height: 30),
                  Padding(
                    padding: EdgeInsets.symmetric(horizontal: 24),
                    child: Column(
                      crossAxisAlignment: CrossAxisAlignment.start,
                      children: <Widget>[
                        RichText(
                          text: TextSpan(
                            style: Theme.of(context).textTheme.display1,
                            children: [
                              TextSpan(text: "List of  "),
                              TextSpan(
                                text: "Projects ",
                                style: TextStyle(fontWeight: FontWeight.bold),
                              ),
                            ],
                          ),
                        ),
                        Padding(
                  padding: EdgeInsets.only(top: .4),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: <Widget>[
                              projectViewCard(size, context)])
                            ),

                        RichText(
                          text: TextSpan(
                            style: Theme.of(context).textTheme.display1,
                            children: [
                              TextSpan(text: "Project  "),
                              TextSpan(
                                text: "Instructor",
                                style: TextStyle(fontWeight: FontWeight.bold),
                              ),
                            ],
                          ),
                        ),
                        SizedBox(height: 20),
                        
                      Padding(
                        padding: EdgeInsets.only(top: .4),
                         child: Column(
                           children: <Widget>[ 
                            InstructorCard(name: "akshay",subject: "InstructorCard",size:size),
                               SizedBox(height: 20),

                           ],
                         ), 

                      ),
                        SizedBox(height: 140),
                      ],
                    ),
                  ),
                ],
              ),
            ),
          ],
        ),
      ),
    );
  }

  

  Container projectViewCard(Size size, BuildContext context) {
    return Container(
      margin: EdgeInsets.symmetric(vertical: 20),
      width: double.infinity,
      height: 205,
      child: Stack(
        children: <Widget>[
          Positioned(
            bottom: 0,
            left: 0,
            right: 0,
            child: Container(
              padding: EdgeInsets.only(
                left: 24,
                top: 24,
                right: size.width * .35,
              ),
              height: 185,
              width: double.infinity,
              decoration: BoxDecoration(
                color: cardGreen,
                borderRadius: BorderRadius.circular(29),
              ),
              child: Column(
                crossAxisAlignment: CrossAxisAlignment.start,
                children: <Widget>[
                  Text(
                    "4th June 2020",
                    style: TextStyle(
                      fontSize: 9,
                      color: kLightBlackColor,
                    ),
                  ),
                  SizedBox(height: 5),
                  Text(
                    "How To Win \nFriends &  Influence",
                    style: Theme.of(context).textTheme.title,
                  ),
                  Text(
                    "Akshay Bhadange",
                    style: TextStyle(color: kLightBlackColor),
                  ),
                  SizedBox(height: 10),
                  Row(
                    children: <Widget>[
                      BookRating(score: 4.9),
                      SizedBox(width: 10),
                      Expanded(
                        child: Text(
                          "When the earth was flat and everyone wanted to win the game of the best and people….",
                          maxLines: 3,
                          overflow: TextOverflow.ellipsis,
                          style: TextStyle(
                            fontSize: 10,
                            color: kLightBlackColor,
                          ),
                        ),
                      ),
                    ],
                  )
                ],
              ),
            ),
          ),
          Positioned(
            right: 0,
            top: 0,
            child: Image.asset(
              "assets/images/book-3.png",
              width: size.width * .37,
            ),
          ),
          Positioned(
            bottom: 0,
            right: 0,
            child: SizedBox(
              height: 40,
              width: size.width * .3,
            
              child: TwoSideRoundedButton(
                text: "View",
                radious: 24,  
                press: () {
                  Navigator.push(
                              context,
                              MaterialPageRoute(
                                builder: (context) {
                                  return DetailsScreen();
                                },
                              ),
                            );

                },
              ),
            ),
          ),
        ],
      ),
    );
  }
}
