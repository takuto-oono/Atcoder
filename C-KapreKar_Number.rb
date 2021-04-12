def digits(n)
    return n.to_s.length
end
def digits_number(n, nums)
    n = n.to_s
    nums = n.chars
    return nums
end

def g1(digit, nums)
    nums = nums.sort.reverse
    ans = 0
    for i in 0..digit - 1 do
        ans += nums[i].to_i * (10 ** (digit - i - 1))
    end
    return ans
end

def g2(digit, nums)
    nums = nums.sort
    ans = 0
    for i in 0..digit - 1 do
        ans += nums[i].to_i * (10 ** (digit - i - 1))
    end
    return ans
end

def f(x, y)
    return x - y
end

n, k = gets.split(' ').map(&:to_i)

(1..k).each do |i| 
    nums = []
    digit = digits(n)
    nums = digits_number(n, nums)
    x = g1(digit, nums)
    y = g2(digit, nums)
    
    n = f(x, y)
end

puts n


