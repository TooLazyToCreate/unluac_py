SomeJunkTable = {
    x = 0,
    y = 0,
    DoThisForAWhile = function(self, end_pos)
        while self.x ~= end_pos.x or self.y ~= end_pos.y do
            if math.abs(self.x - end_pos.x) > math.abs(self.y - end_pos.y) then
                self.x = self.x - (self.x > end_pos.x and 1 or -1)
            else
                self.y = self.y - (self.y > end_pos.y and 1 or -1)
            end
            print(self.x, self.y)
        end
    end
}

setmetatable(SomeJunkTable, {
    __index = function(self, a)
        return _G[a]
    end
})

function some_junk_func(a)
    local a = a or 10
    local r = {}
    for i=a,1,-1 do
        table.insert(r, tostring(i))
    end
    for i, v in ipairs(r) do
        print(i, v)
    end
end

SomeJunkTable:DoThisForAWhile({
    x = 10,
    y = -10
})
SomeJunkTable["some_junk_func"](10)
