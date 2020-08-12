/*
  问题1：找到两个数组的交集

  var firstArray = [2, 2, 4, 1];
  var secondArray = [1, 2, 0, 2];

  intersection(firstArray, secondArray); // [2, 1]
*/

function intersection(firstArray, secondArray) {
  return [...new Set(firstArray.filter(item => secondArray.includes(item)))];
}

/*
  问题2：实现一个 URL 解析参数的方法
  比如：parse('https://www.aliexpress.com?a=1&b=2#p=bottom')
  返回：
  {
    query: {
      a: 1,
      b: 2
    },
    hash: {
      p: 'bottom'
    }
  }
*/

function parse(url) {
  if (typeof url !== 'string' || url.length === 0) return {};
  const pattern = /[^?#]+(\?)?([^?#]*)#?(.*)/;
  const result = url.match(pattern);
  if (result && result.length > 3) {
    const searchStr = result[2];
    const hashStr = result[3];
    const parseEqual = arr => arr.reduce((prev, item) => {
      const [key, value] = item.split('=');
      prev[key] = value;
      return prev;
    }, {})
    const query = parseEqual(searchStr.split('&'));
    const hash = parseEqual([hashStr]);
    return {
      query,
      hash
    }
  }
  return {};
}

/* 
  问题3：请根据面对对象编程的思想，设计一个类型 Cash 用于表达人民币，使得：
  class Cash {
  }
  const cash1 = new Cash(105);
  const cash2 = new Cash(66);
  const cash3 = cash1.add(cash2);
  const cash4 = Cash.add(cash1, cash2);
  const cash5 = new Cash(cash1 + cash2);
  console.log(`${cash3}`, `${cash4}`, `${cash5}`);
  // 在以上代码执行的时候，输出结果为：
  // 1元7角1分, 1元7角1分, 1元7角1分
*/

class Cash {
  constructor(val) {
    this.value = val;
  }
  
  add(cash) {
    if (cash instanceof Cash) {
      return newthis.value + cash.value;
    }
  }
  
  static add(...rest) {
    if (rest.every(item => item instanceof Cash)) {
      return new Cash(rest.reduce((prev, item) => {
        prev += item;
        return prev;
      },0))
    }
    return null;
  }
  
  toString() {
    const strValue = String(this.value);
  	return `${strValue.charAt(0)}元${strValue.charAt(1)}角${strValue.charAt(2)}分`
  }

  [Symbol.toPrimitive]() 
}