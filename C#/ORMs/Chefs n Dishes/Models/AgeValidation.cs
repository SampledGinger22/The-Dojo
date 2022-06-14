namespace Chefs_n_Dishes.Models;
using System.ComponentModel.DataAnnotations;
using System.ComponentModel.DataAnnotations.Schema;
#pragma warning disable CS8618

public class MinimumAgeAttribute : ValidationAttribute
{
    int _minimumAge;
    public MinimumAgeAttribute(int minimumAge)
    {
        _minimumAge = minimumAge;
    }
    public override bool IsValid(object? value)
    {
        if(value != null)
        {
            DateTime date;
            if (DateTime.TryParse(value.ToString(), out date))
            {
                return date.AddYears(_minimumAge) < DateTime.Now;
            }
            return false;
        }
        else return false;
    }
}