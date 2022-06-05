List<object> templist = new List<object>();

templist.Add(7);
templist.Add(28);
templist.Add(-1);
templist.Add(true);
templist.Add("Chair"); 

int sum = 0;
foreach(object val in templist) {
    if(val is int) {
        Console.WriteLine(val);
        sum += (int)val;
    }
    else if(val is bool) {
        Console.WriteLine(val);
    }
    else if(val is string){
        Console.WriteLine(val);
    }
}
Console.WriteLine(sum);
