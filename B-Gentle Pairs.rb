n = gets.chomp.to_i
XY = []
for i in 0..n - 1
    xy = gets.split(" ").map(&:to_i)
    XY.push(xy)
end

ans = 0
(0...n - 1).each do |i|
    (i + 1...n - 1).each do |j|
        x1 = XY[i][0]
        x2 = XY[j][0]
        y1 = XY[i][1]
        y2 = XY[j][1]
        z = (y1 - y2) / (x1 - x2)
            
        if z >= -1 && z <= 1
            ans += 1
        end
        
    end
end
puts ans



