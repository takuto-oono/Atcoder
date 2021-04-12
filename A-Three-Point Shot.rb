x, y = gets.split(' ').map(&:to_i)
z = (x - y).abs
if z < 3
    ans = 'Yes'
    
else
    ans = 'No'   

end
puts ans
