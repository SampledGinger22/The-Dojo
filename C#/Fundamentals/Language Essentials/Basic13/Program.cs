
// Function 1
// static void PrintNumbers(){
//     for(int i = 1; i <= 255; i++){
//         Console.WriteLine(i);
//     }
// }
// PrintNumbers();

// Function 2
// static void PrintOdds(){
//     for(int i = 1; i <= 255; i++){
//         if(i%2!=0){
//             Console.WriteLine(i); 
//         }
//     }
// }
// PrintOdds();

// Function 3
// static void PrintSum(){
//     int sum = 0;
//     for(int i = 0; i <= 255; i++){
//         sum += i;
//     }
//     Console.WriteLine(sum);
// }
// PrintSum();

// Function 4
// static void LoopArray(int[] numbers){
//     foreach(int num in numbers){
//         Console.WriteLine(num);
//     }
// }

// int[] sample = {3,2,5,1,5,6,3};
// LoopArray(sample);

// Function 5
// static void FindMax(int[] numbers){
//     int MaxVal = numbers[0];
//     foreach(int num in numbers){
//         if(num > MaxVal){
//             MaxVal = num;
//         }
//     }
//     Console.WriteLine(MaxVal);
// }

// int[] list = {-23, -1, -5, -6};
// FindMax(list);

// Function 6
// static void GetAverage(int[] numbers){
//     int len = numbers.Count();
//     int total = 0;
//     foreach(int num in numbers){
//         total += num;
//     }
//     int avg = total / len;
//     Console.WriteLine(avg);
// }

// int[] list2 = {1,2,3,4,5,6,7,8,9,10};
// GetAverage(list2);

//funtion 7
// static void OddArray(){
//     List<int> array = new List<int>();
//     for(int i = 0; i <= 255; i++){
//         if(i%2!=0){
//             array.Add(i);
//             Console.WriteLine(i);
//         }
//     }
//     int[] finalarr = array.ToArray();
// }
// OddArray();

// function 8
// static void GreaterThanY(int[] numbers, int y){
//     int count = 0;
//     for(int i = 0; i < numbers.Count(); i++){
//         if(numbers[i] > y){
//             count += 1;
//         }
//     }
//     Console.WriteLine(count);
// }

// int[] nums = {32,5,7,14,16,32,33,65};
// GreaterThanY(nums, 15);

//Fuction 9
// static void SquareArrayValues(int[] numbers){
//     for(int i = 0; i < numbers.Count(); i++){
//         Console.WriteLine(numbers[i]);
//         numbers[i] *= numbers[i];
//         Console.WriteLine(numbers[i]);
//     }
// }
// int[] nums = {1,5,10,-10};
// SquareArrayValues(nums);

//Function 10
// static void EliminateNegatives(int[] numbers){
//     List<int> list = new List<int>();
//     for(int i = 0; i < numbers.Count(); i++) {
//         if(numbers[i] > 0){
//             list.Add(numbers[i]);
//             Console.WriteLine(numbers[i]);
//         }
//         else {
//         list.Add(0);
//         Console.WriteLine(0);
//         }
//     }
//     int[] positives = list.ToArray();
// }

// int[] nums = {1,-3,5,10,-2};
// EliminateNegatives(nums);

//Function 11
// static void MinMaxAverage(int[] numbers){
//     int MinVal = numbers[0];
//     int MaxVal = numbers[0];
//     int total = 0;
//     for(int i = 0; i < numbers.Count(); i++){
//         if(numbers[i] > MaxVal){
//             MaxVal = numbers[i];
//         }
//         if(numbers[i] < MinVal){
//             MinVal = numbers[i];
//         }
//         total += numbers[i];
//     }
//     int Avg = total / numbers.Count();
//     Console.WriteLine(MaxVal.ToString());
//     Console.WriteLine(MinVal.ToString());
//     Console.WriteLine(Avg.ToString());
// }

// int[] nums = {1,5,10,-2};
// MinMaxAverage(nums);

//Function 12
// int[] nums = {3,5,6,1,7,5,3,6,5};
// static void ShiftValues(int[] numbers){
//     numbers[0] = numbers[1];
//     Console.WriteLine(numbers[0]);
//     for(int i = 1; i < numbers.Length-1; i++){
//         numbers[i] = numbers[i+1];
//         Console.WriteLine(numbers[i]);
//     }
//     numbers[numbers.Length-1] = 0;
//     Console.WriteLine(numbers[numbers.Length-1]);
// }
// ShiftValues(nums);

//Function 13
// static void NumToString(int[] numbers){
//     List<object> list = new List<object>();
//     for(int i = 0; i < numbers.Length; i++){
//         if(numbers[i] < 0){
//             list.Add("Dojo");
//             Console.WriteLine("Dojo");
//         }
//         else {
//             list.Add(numbers[i]);
//             Console.WriteLine(numbers[i].ToString());
//         }
//     }
// }

// int[] nums = {-1, -2, 2};
// NumToString(nums);