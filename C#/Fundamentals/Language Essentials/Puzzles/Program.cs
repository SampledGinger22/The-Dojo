// static void RandomArray(){
//     int[] arr = new int[10];
//     Random Rand = new Random();
//     for(int i = 0; i < 10; i++){
//         arr[i] = Rand.Next(5,26);
//     }
//     int MaxVal = arr[0];
//     int MinVal = arr[0];
//     int Sum = arr[0];
//     for(int j = 1; j < arr.Length-1; j++){
//         if(arr[j] > MaxVal){
//             MaxVal = arr[j];
//         }
//         if(arr[j] < MinVal){
//             MinVal = arr[j];
//         }
//         Sum += arr[j];
//     }
//     Console.WriteLine(MaxVal.ToString());
//     Console.WriteLine(MinVal.ToString());
//     Console.WriteLine(Sum.ToString());
// }
// RandomArray();

// static void TossCoin(int num){
//     int FlipCount = num;
//     int i = 0;
//     while(i < FlipCount){
//         i++;
//         Console.WriteLine("Tossing a Coin!");
//         Random rand = new Random();
//         int flip = rand.Next(0, 2);
//         if(flip == 1){
//             Console.WriteLine("Heads");
//         }
//         if(flip == 0){
//             Console.WriteLine("Tails");
//         }
//     }
// }
// TossCoin(5);

static void Names(){
    List<string> allnames = new List<string>();
    allnames.Add("Tiffany");
    allnames.Add("Charlie");
    allnames.Add("Todd");
    allnames.Add("Geneva");
    allnames.Add("Sydney");

    List<string> namelength = new List<string>();
    for(int i = 0; i < allnames.Count(); i++){
        string tempname = allnames[i];
        if(tempname.Length > 4){
            namelength.Add(tempname);
        }
    }
    for(int i = 0; i < namelength.Count(); i++){
        Console.WriteLine(namelength[i]);
    }
}
Names();