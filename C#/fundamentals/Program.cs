using System;

namespace fundamentals
{
    class Program
    {
        static void Main(string[] args)
        {
            ///print integers 1-255
            ///for (int i = 1; i < 256; i += 1){
                ///Console.WriteLine(i);
            ///}

            ///values divisible by 3 or 5, but not both
            ///for (int i = 1; i < 101; i += 1){
                ///if(!(i % 15 == 0)){
                    ///if (i % 3 == 0 || i % 5 == 0){
                        ///Console.WriteLine(i);
                    ///};
                ///};
            ///};

           ///modify ^ for 3 = fizz buzz = 5 fizzbuzz = 15
           for (int i = 1; i < 101; i += 1){
               if (i % 15 == 0){
                   Console.WriteLine("FizzBuzz");
               }
                else if (i % 3 == 0){
                    Console.WriteLine("Fizz");
                }
                else if (i % 5 == 0){
                    Console.WriteLine("Buzz");
               }
           } 
        }
    }
}
