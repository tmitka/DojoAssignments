using System;
using System.Collections.Generic;
namespace collections

{
    class Program
    {
        static void Main(string[] args)
        {
            ///int[] nineArray = {0,1,2,3,4,5,6,7,8,9};
            string[] nameArray = {"Tim", "Martin", "Nikki", "Sara"};
            ///bool[] boolArray = {true, false, true, false, true, false, true, false, true, false};

            ///int [,] multtable = new int[10,10];
            ///{
                ///{1,2,3,4,5,6,7,8,9,10}
            ///}
            ///Console.WriteLine(multtable[0, 1]);

            List<string> flavors = new List<string>();

            flavors.Add("Vanilla");
            flavors.Add("Chocolate");
            flavors.Add("Strawberry");
            flavors.Add("Mackinac Island Fudge");
            flavors.Add("Mint");
            Console.WriteLine(flavors.Count);
            Console.WriteLine(flavors[2]);
            flavors.RemoveAt(2);
            Console.WriteLine(flavors.Count);

            Random rand = new Random();

            Dictionary<string,string> user = new Dictionary<string,string>();
            for (int i = 0; i < nameArray.Length; i += 1){
                int r = rand.Next(flavors.Count);
                user.Add(nameArray[i], flavors[r]);
            }
            foreach (var entry in user){
                Console.WriteLine(entry.Key + "-" + entry.Value);
            }
        }
    }
}
