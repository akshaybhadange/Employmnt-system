import 'package:flutter/material.dart';
import 'package:book_app/constants.dart';

class InstructorCard extends StatelessWidget {


  final String name ;
  final String subject;
  final Size size;

  const InstructorCard({
      Key key,
      this.size,  
      this.name,
      this.subject,
  }
  
   ) : super(key: key  )  ;

  
   

  @override
  Widget build(BuildContext context) {
   return Container(
                        height: 80,
                        width: double.infinity,
                        decoration: BoxDecoration(
                          color: Colors.white,
                          borderRadius: BorderRadius.circular(38.5),
                          boxShadow: [
                            BoxShadow(
                              offset: Offset(0, 10),
                              blurRadius: 33,
                              color: Color(0xFFD3D3D3).withOpacity(.84),
                            ),
                          ],
                        ),
                        child: ClipRRect(
                          borderRadius: BorderRadius.circular(38.5),
                          child: Column(
                            crossAxisAlignment: CrossAxisAlignment.start,
                            children: <Widget>[
                              Expanded(
                                child: Padding(
                                  padding:
                                      EdgeInsets.only(left: 30, right: 20,bottom: 10),
                                  child: Row(
                                    children: <Widget>[
                                      Expanded(
                                        child: Column(
                                          mainAxisAlignment:
                                              MainAxisAlignment.end,
                                          crossAxisAlignment:
                                              CrossAxisAlignment.start,
                                          children: <Widget>[
                                            Text(
                                              subject,
                                              style: TextStyle(
                                                fontWeight: FontWeight.bold,
                                              ),
                                            ),
                                            Text(
                                              name,
                                              style: TextStyle(
                                                color: kLightBlackColor,
                                              ),
                                            ),
                                            Align(
                                              alignment:
                                                  Alignment.bottomRight,
                                               
                                            ),
                                            SizedBox(height: 5),
                                          ],
                                        ),
                                      ),
                                      Image.asset(
                                        "assets/images/book-1.png",
                                        width: 55,
                                      )
                                    ],
                                  ),
                                ),
                              ),
                              Container(
                                height: 7,
                                width: size.width * .65,
                                decoration: BoxDecoration(
                                  color: kProgressIndicator,
                                  borderRadius: BorderRadius.circular(7),
                                ),
                              ),
                            ],
                          ),
                        ),
                      );
  }
}