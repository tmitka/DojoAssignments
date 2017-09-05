using System;
using System.Collections.Generic;
namespace basic13
{
    public class Program
    {
        public static void count(){
            for (int i = 1; i < 256; i += 1){
                Console.WriteLine(i);
            }

        }
        public static void countodd(){
            for (int i = 1; i < 256; i+= 1){
                if(i % 2 != 0){
                    Console.WriteLine(i);
                }
            }
        }

        public static void printSum(){
            int sum = 0;
            for (int i = 0; i < 256; i+= 1){
                sum += i;
                Console.WriteLine("New number:" + i + " Sum:" + sum);
            }
        }
        public static void iterArr(int[] X){
            for (int i = 0; i < X.Length; i += 1){
                Console.WriteLine(X[i]);
            }

        }

        public static int findmax(int[] arr){
            int max = arr[0];
            for (int i = 1; i < arr.Length; i += 1){
                if (arr[i] > max){
                    max = arr[i];
                }
            }
            return max;
        }

        public static int findavg(int[] arr){
            int avg = 0;
            int sum = arr[0];
            for (int i = 1; i < arr.Length; i += 1){
                sum += arr[i];
            }
            avg = sum/arr.Length;
            return avg;
            
        }

        public static void oddarr(){
            List<int> intList = new List<int>();
            for (int i = 1; i < 256; i += 1){
                if (i % 2 != 0){
                    intList.Add(i);
                }
            }
            int[] intarr = intList.ToArray();
            foreach (int num in intarr){
                Console.WriteLine(num);
            }
        }
        public static void greaterY(int[] arr, int y){
            List<int> intList = new List<int>();
            for (int i = 0; i < arr.Length; i += 1){
                if (arr[i] > y){
                    intList.Add(i);
                }
            }
            int[] intarr = intList.ToArray();
            foreach (int num in intarr){
                Console.WriteLine(num);
            }
        }

        public static void nonegative(int[] arr){
            for (int i = 0; i < arr.Length; i += 1){
                if (arr[i] < 0){
                    arr[i] = 0;
                }
            }
            foreach (int num in arr){
                Console.WriteLine(num);
            }
        }

        public static void square(int[] arr){
            for (int i = 0; i < arr.Length; i += 1){
                arr[i] = arr[i] * arr[i];
                }
            
            foreach (int num in arr){
                Console.WriteLine(num);
            }
        }

        public static void minmaxavg(int[]arr){
            int max = arr[0];
            int min = arr[0];
            int avg = arr[0];
            int sum = 0;
            for (int i = 1; i < arr.Length; i += 1){
                if (arr[i] > max){
                    max = arr[i];
                }
                else if (arr[i] < min){
                    min = arr[i];
                }
                sum += arr[i];
            }
            avg = sum/arr.Length;
            Console.WriteLine(min);
            Console.WriteLine(max);
            Console.WriteLine(avg);
        }
        public static object[] numtostr(object[] arr){
            for (int i = 0; i < arr.Length; i += 1){
                if ((int)arr[i] < 0){
                    arr[i] = "Dojo";
                }
            }
            return arr;
        }
        
        public static void Main(string[] args)
        {
            ///count();
            ///countodd();
            ///printSum();
            ///int[] X = {1, 3, 5,7,9,13};
            ///iterArr(X);
            //int[] arr = {-3, -5, -7};
            //Console.WriteLine(findmax(arr));
            //int[] arr = {2,10,3};
            //Console.WriteLine(findavg(arr));
            //oddarr();
            //int[] arr = {1,3,5,7};
            //greaterY(arr, 3);
            ///int[] arr = {1,5,10,-2};
            ///nonegative(arr);
            //int[] arr = {1,5,10,-2};
            //square(arr);
            //int[] arr = {1,5,10,-2};
           // minmaxavg(arr);
           object[] arr = new object[] {-1,-3,2};
           numtostr(arr);

        }
    }
}
