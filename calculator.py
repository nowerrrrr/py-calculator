while True:
     print("""
                                             $$\                     $$\            $$\                         
                                             $$ |                    $$ |           $$ |                        
 $$$$$$\  $$\   $$\        $$$$$$$\ $$$$$$\  $$ | $$$$$$$\ $$\   $$\ $$ | $$$$$$\ $$$$$$\    $$$$$$\   $$$$$$\  
$$  __$$\ $$ |  $$ |      $$  _____|\____$$\ $$ |$$  _____|$$ |  $$ |$$ | \____$$\\_$$  _|  $$  __$$\ $$  __$$\ 
$$ /  $$ |$$ |  $$ |      $$ /      $$$$$$$ |$$ |$$ /      $$ |  $$ |$$ | $$$$$$$ | $$ |    $$ /  $$ |$$ |  \__|
$$ |  $$ |$$ |  $$ |      $$ |     $$  __$$ |$$ |$$ |      $$ |  $$ |$$ |$$  __$$ | $$ |$$\ $$ |  $$ |$$ |      
$$$$$$$  |\$$$$$$$ |      \$$$$$$$\\$$$$$$$ |$$ |\$$$$$$$\ \$$$$$$  |$$ |\$$$$$$$ | \$$$$  |\$$$$$$  |$$ |      
$$  ____/  \____$$ |       \_______|\_______|\__| \_______| \______/ \__| \_______|  \____/  \______/ \__|      
$$ |      $$\   $$ |                                                                                            
$$ |      \$$$$$$  |                                                                                            
\__|       \______/                                                                                             
          """)
     print ("discord--->turquoisevr\n   ")
     print ("opperation--->add,mul,div,sub")
           
     num1 = input("enter a number: ")
     method = input("what opperation should i perform? : ")
     num2 = input("enter a number: ")
     
     result1 = float(num1) + float(num2)
     result2 = float(num1) / float(num2)
     result3 = float(num1) * float(num2)
     result4 = float(num1) - float(num2)
     
     if method == "add":
          print (result1)
     elif method == "div": 
          print (result2)
     elif method == "mul":
          print (result3)
     elif method == "sub":
          print (result4)
         
         