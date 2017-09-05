using System;
using System.Collections.Generic;
namespace boxing
{
    class Program
    {
        static void Main(string[] args)
        {
            List<object> objlist = new List<object>();
            int sum = 0;
            objlist.Add(7);
            objlist.Add(28);
            objlist.Add(-1);
            objlist.Add(true);
            objlist.Add("chair");
            for (var i = 0; i < objlist.Count; i += 1){
                Console.WriteLine(objlist[i]);
                if (objlist[i] is int){
                    int value = System.Convert.ToInt32(objlist[i]);
                    sum += value;
                }
            }
            Console.WriteLine(sum);
        }
    }
}
