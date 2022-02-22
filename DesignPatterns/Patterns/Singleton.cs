using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DesignPatterns.Patterns
{
    public class Singleton
    {
        private static Singleton instance;
        private List<string> nameList = new();
        private Singleton()
        {
        }

        public static Singleton getInstance()
        {
            if(Singleton.instance is null)
            {
                Singleton.instance = new Singleton();
            }
            return Singleton.instance;
        }

        public List<string> getNameList()
        {
            return this.nameList;
        }
    }
}
