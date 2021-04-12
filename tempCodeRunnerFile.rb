n = gets.chomp.to_i
XY = []
for i in 0..n
    xy = gets.split(" ").map(&:to_i)
    XY.push(xy)
end

ans = 0
(0...n).each do |i|
    (i + 1...n).each do |j|
        x1 = XY[i][0]
        x2 = XY[j][0]
        y1 = XY[i][1]
        y2 = XY[j][1]
        z = (y1 - y2) / (x1 - x2)
        puts z
            
        if z >= -1 && z <= 1
            ans += 1
        end
        
    end
end
puts ans



