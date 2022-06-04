int[] count = {0,1,2,3,4,5,6,7,8,9};
string[] names = new string[] {"Tim", "Martin", "Nikki", "Sara"};
bool[] alternating = new bool[10];
    for(int i = 0; i<alternating.Length; i++){
        if(i%2!=0){
            alternating[i] = false;
        }
        else alternating[i] = true;
    }

List<string> icecream = new List<string>();
icecream.Add("Chocolate");
icecream.Add("Strawberry");
icecream.Add("Rocky Road");
icecream.Add("Vanilla");
icecream.Add("Moose Tracks");
int creamlength = icecream.Count;
// Console.WriteLine(creamlength.ToString());
// Console.WriteLine(icecream[2].ToString());
// icecream.Remove("Rocky Road");
int newcreamlength = icecream.Count;
// Console.WriteLine(newcreamlength.ToString());

Dictionary<string,string> tasteprofile = new Dictionary<string, string>();
tasteprofile.Add(names[0], icecream[0]);
tasteprofile.Add(names[1], icecream[1]);
tasteprofile.Add(names[2], icecream[2]);
tasteprofile.Add(names[3], icecream[3]);

Console.WriteLine("Tim - " + tasteprofile["Tim"]);
Console.WriteLine("Martin - " + tasteprofile["Martin"]);
Console.WriteLine("Nikki - " + tasteprofile["Nikki"]);
Console.WriteLine("Sara - " + tasteprofile["Sara"]);